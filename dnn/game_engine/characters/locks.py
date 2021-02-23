"""This file provides with CharacterLock base classes.

"""

__all__ = ['CharacterLockBase']


class CharacterLockBase(object):
    """
    Base class for Character locks.
    """

    def __init__(self, character=None, lock_reason=None):
        """
        :param character:
        :param lock_reason:
        """
        self.character = character
        self.lock_reason = lock_reason

    def destroy(self):
        pass
