from cinder.exception import VolumeDriverException
from cinder.i18n import _


class NexentaException(VolumeDriverException):
    message = _("%(message)s")