import logging
import requests

from okopilote.devices.common.abstract import AbstractTemperatureSensor

logger = logging.getLogger(__name__)


def from_conf(conf):
    return BoilerSensor(conf.get("url"))


class BoilerSensor(AbstractTemperatureSensor):
    def __init__(self, url):
        self.url = url

    @property
    def temperature(self):
        r = requests.get(self.url, verify=False, timeout=5)
        r.raise_for_status()
        try:
            return float(r.text)
        except ValueError:
            logger.error("temperature: expected a float number, got '{r}'")
            raise
