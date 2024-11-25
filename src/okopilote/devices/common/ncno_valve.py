from . import devices


def from_conf(conf):
    return NCNOValve(
        conf.getboolean("normally_open"),
        devices.get_device(conf["relay_device"]),
        opening_time=conf.getint("opening_time", None),
        closing_time=conf.getint("closing_time", None),
    )


class NCNOValve:
    """Normally closed or normally opened valve"""

    def __init__(
        self, normally_open, relay_device, opening_time=None, closing_time=None
    ):
        self.normally_open = normally_open
        self.relay = relay_device
        self.opening_time = opening_time
        self.closing_time = closing_time

    def close(self):
        if self.normally_open:
            self.relay.switch_on()
        else:
            self.relay.switch_off()

    def open(self):
        if self.normally_open:
            self.relay.switch_off()
        else:
            self.relay.switch_on()

    def release(self):
        self.relay.switch_off()

    def is_opened(self):
        return self.relay.is_on() is not self.normally_open
