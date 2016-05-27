from cinder.exception import VolumeDriverException


class NexentaException(VolumeDriverException):
    message = _("%(message)s")