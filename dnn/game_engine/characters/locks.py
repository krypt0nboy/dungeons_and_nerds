"""This file provides with CharacterLock base classes.

"""

__all__ = ['CharacterLocksRegistry', 'CharacterLocksRegistryController', 'CharacterLockBase']


class CharacterLocksRegistry(object):
    """
    """

    def __init__(self, **kwargs):
        self._locks = []

    @property
    def locks(self):
        return self._locks

    @locks.setter
    def locks(self, lock):
        self._locks.append(lock)


class CharacterLocksRegistryController(object):
    """
    """

    def __init__(self, lock_registry=None):
        self._lock_registry = lock_registry

    def register_lock(self, character=None, lock_reason=None):
        self._lock_registry.locks = CharacterLockBase(character=character, lock_reason=lock_reason)


class CharacterLockBase(object):
    """
    Base class for Character locks.
    """

    def __init__(self, character=None, lock_reason=None, start_datetime=None):
        """
        :param character:
        :param lock_reason:
        """
        self.character = character
        self.lock_reason = lock_reason
        self.start_datetime = start_datetime
