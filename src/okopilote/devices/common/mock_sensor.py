from .abstract import AbstractTemperatureHumiditySensor


def from_conf(conf):
    try:
        t = conf.getfloat("temperature")
    except ValueError:
        t = None
    try:
        h = conf.getfloat("humidity")
    except ValueError:
        h = None
    return FakeSensor(temperature=t, humidity=h)


class MockSensor(AbstractTemperatureHumiditySensor):
    """Mock sensor returning static temperature and humidity values"""

    def __init__(self, temperature=None, humidity=None):
        self.temp = temperature
        self.humi = humidity

    @property
    def humidity(self):
        if self.humi is None:
            raise NotImplementedError("Not a humidity sensor")
        else:
            return self.humi

    @property
    def temperature(self):
        if self.temp is None:
            raise NotImplementedError("Not a temperature sensor")
        else:
            return self.temp

    @property
    def temperature_humidity(self):
        return (self.temperature, self.humidity)
