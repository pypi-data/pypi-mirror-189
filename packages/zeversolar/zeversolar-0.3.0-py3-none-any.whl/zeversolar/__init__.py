import dataclasses
import typing
import urllib.parse
from datetime import datetime, timedelta
from enum import Enum, IntEnum
from dataclasses import MISSING

import requests

from zeversolar.exceptions import ZeverSolarTimeout, ZeverSolarHTTPError, ZeverSolarHTTPNotFound, ZeverSolarNotSupported

kWh = typing.NewType("kWh", float)
Watt = typing.NewType("Watt", int)


class PowerMode(IntEnum):
    ON = 0
    OFF = 1


class Values(IntEnum):
    WIFI_ENABLED = 0  # bool 0-1
    MAC_ADDRESS = 2
    REGISTRY_KEY = 3  # string
    HARDWARE_VERSION = 4  # string
    SOFTWARE_VERSION = 5  # string
    COMMUNICATION_STATUS = 8  # bool 0-1
    SERIAL_NUMBER = 10  # string
    REPORTED_TIME = 6  # hh:mm
    REPORTED_DATE = 7  # dd/mm/yyyy


class M10Values(IntEnum):
    PAC = 12  # WATT
    ENERGY_TODAY = 13  # kWh
    STATUS = 14  # enum

    @property
    def supported_hardware_version(self):
        return "M10"


class M11Values(IntEnum):
    PAC = 11  # WATT
    ENERGY_TODAY = 12  # kWh
    STATUS = 13  # enum

    @property
    def supported_hardware_version(self):
        return "M11"


class StatusEnum(Enum):
    OK = "OK"
    ERROR = "ERROR"


@dataclasses.dataclass
class ZeverSolarData:
    wifi_enabled: bool
    mac_address: str
    registry_key: str
    hardware_version: str
    software_version: str
    communication_status: bool
    serial_number: str
    pac: Watt
    energy_today: kWh
    status: StatusEnum
    reported_datetime: datetime


class ZeverSolarParser:
    def __init__(self, zeversolar_response: str):
        self.zeversolar_response = zeversolar_response

    def _get_value(self, value: IntEnum) -> str:
        response_parts = self.zeversolar_response.split()
        return response_parts[value.value]

    def parse(self):
        wifi_enabled = bool(self._get_value(Values.WIFI_ENABLED))
        mac_address = self._get_value(Values.MAC_ADDRESS)
        registry_key = self._get_value(Values.REGISTRY_KEY)
        hardware_version = self._get_value(Values.HARDWARE_VERSION)
        software_version = self._get_value(Values.SOFTWARE_VERSION)
        communication_status = bool(self._get_value(Values.COMMUNICATION_STATUS))
        serial_number = self._get_value(Values.SERIAL_NUMBER)

        if hardware_version.upper() == "M10":
            hardware_specific_values = M10Values
        elif hardware_version.upper() == "M11":
            hardware_specific_values = M11Values
        else:
            raise ZeverSolarNotSupported(f"This {hardware_version=} is not yet supported")

        pac = Watt(int(self._get_value(hardware_specific_values.PAC)))
        energy_today = kWh(self._fix_leading_zero(self._get_value(hardware_specific_values.ENERGY_TODAY)))
        status = StatusEnum(self._get_value(hardware_specific_values.STATUS))
        reported_time = self._get_value(Values.REPORTED_TIME)
        reported_date = self._get_value(Values.REPORTED_DATE)

        reported_datetime = datetime.strptime(f"{reported_date} {reported_time}", "%d/%m/%Y %H:%M")

        return ZeverSolarData(
            wifi_enabled=wifi_enabled,
            mac_address=mac_address,
            registry_key=registry_key,
            hardware_version=hardware_version,
            software_version=software_version,
            communication_status=communication_status,
            serial_number=serial_number,
            pac=pac,
            energy_today=energy_today,
            status=status,
            reported_datetime=reported_datetime,
        )

    @staticmethod
    def _fix_leading_zero(string_value: str) -> float:
        split_values = string_value.split(".")
        if len(decimals := split_values[1]) == 1:
            string_value = f"{split_values[0]}.0{decimals}"
        return float(string_value)


class ZeverSolarClient:
    def __init__(self, host: str):
        if "http" not in host:
            # noinspection HttpUrlsUsage
            host = f"http://{host}"
        self.host = urllib.parse.urlparse(url=host).netloc.strip("/")
        self._timeout = timedelta(seconds=5).total_seconds()
        self._serial_number = MISSING

    def get_data(self) -> ZeverSolarData:
        response = requests.get(url=f"http://{self.host}/home.cgi", timeout=self._timeout)
        try:
            response.raise_for_status()
        except requests.exceptions.Timeout:
            raise ZeverSolarTimeout()
        except requests.exceptions.HTTPError:
            if response.status_code == 404:
                raise ZeverSolarHTTPNotFound()
            raise ZeverSolarHTTPError()
        return ZeverSolarParser(zeversolar_response=response.text).parse()

    def power_on(self):
        return self.ctrl_power(mode=PowerMode.ON)

    def power_off(self):
        return self.ctrl_power(mode=PowerMode.OFF)

    def ctrl_power(self, mode: PowerMode):
        if self._serial_number is MISSING:
            self._serial_number = self.get_data().serial_number

        response = requests.post(
            url=f"http://{self.host}/inv_ctrl.cgi",
            data={'sn': self._serial_number, 'mode': mode.value},
            timeout=self._timeout,
        )
        try:
            response.raise_for_status()
        except requests.exceptions.Timeout:
            raise ZeverSolarTimeout()
        except requests.exceptions.HTTPError:
            if response.status_code == 404:
                raise ZeverSolarHTTPNotFound()
            raise ZeverSolarHTTPError()
