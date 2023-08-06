"""Abode lock device."""

from ..helpers import constants as CONST
from . import base


class Lock(base.Device):
    """Class to represent a door lock."""

    implements = CONST.TYPE_LOCK

    def lock(self):
        """Lock the device."""
        success = self.set_status(CONST.STATUS_LOCKCLOSED_INT)

        if success:
            self._state['status'] = CONST.STATUS_LOCKCLOSED

        return success

    def unlock(self):
        """Unlock the device."""
        success = self.set_status(CONST.STATUS_LOCKOPEN_INT)

        if success:
            self._state['status'] = CONST.STATUS_LOCKOPEN

        return success

    @property
    def is_locked(self):
        """
        Get locked state.

        Err on side of caution, assume if lock isn't closed then it's open.
        """
        return self.status in CONST.STATUS_LOCKCLOSED
