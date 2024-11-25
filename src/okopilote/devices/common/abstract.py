from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractBoiler(metaclass=ABCMeta):
    """Abstract base class for boilers"""

    # Mandatory properties

    @abstractproperty
    def accept_control(self):
        """True if boiler accepts to be controlled by us"""
        raise NotImplementedError("Must have implemented this property")

    @abstractproperty
    def acquire(self):
        """Acquire data from boiler"""
        raise NotImplementedError("Must have implemented this property")

    @abstractproperty
    def delivering_heat(self):
        """
        True if the central heating system is delivering heat to rooms (water
        circulator is running)
        """
        raise NotImplementedError("Must have implemented this property")

    @abstractproperty
    def generating_heat(self):
        """True if the boiler is generating heat"""
        raise NotImplementedError("Must have implemented this property")

    @abstractproperty
    def heat_available(self):
        """True if heat is immediatly available (without igniting the boiler)"""
        raise NotImplementedError("Must have implemented this property")

    # Mandatory methods

    @abstractmethod
    def force_heating(self, delta=0.0):
        """
        Force the central heating system to deliver heat. When modifying ambiant
        temperature set point, add delta to the new set point
        """
        raise NotImplementedError("Must have implemented this method")

    @abstractmethod
    def release_heating(self):
        """Stop forcing the central heating system"""
        raise NotImplementedError("Must have implemented this method")

    # Optional properties

    @abstractproperty
    def ambiant_temperature(self):
        """Temperature measured by the boiler's ambiant sensor, if any"""
        raise NotImplementedError()


class AbstractHumiditySensor(metaclass=ABCMeta):
    """Abstract base class for humidity sensors"""

    @abstractproperty
    def humidity(self):
        raise NotImplementedError("Must have implemented this property")


class AbstractRelay(metaclass=ABCMeta):
    """Abstract base class for relays"""

    # Mandatory properties

    @abstractproperty
    def is_on(self):
        raise NotImplementedError("Must have implemented this property")

    # Mandatory methods

    @abstractmethod
    def switch_off(self):
        raise NotImplementedError("Must have implemented this method")

    @abstractmethod
    def switch_on(self):
        raise NotImplementedError("Must have implemented this method")


class AbstractTemperatureSensor(metaclass=ABCMeta):
    """Abstract base class for temperature sensors"""

    @abstractproperty
    def temperature(self):
        raise NotImplementedError("Must have implemented this property")


class AbstractTemperatureHumiditySensor(
    AbstractHumiditySensor, AbstractTemperatureSensor
):
    """Abstract base class for sensors combining temperature and humidity"""

    @abstractproperty
    def temperature_humidity(self):
        raise NotImplementedError("Must have implemented this property")
