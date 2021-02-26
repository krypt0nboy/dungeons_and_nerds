"""This file provides with Player base classes.

"""

__all__ = ['PlayerBase']


class PlayerBase(object):
    """
    Base class for Player.
    """

    def __init__(self, nickname=None, active_character=None, active_character_controller=None):
        self._nickname = nickname
        self._active_character = active_character
        self._active_character_controller = active_character_controller

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    def select_character(self, character=None):
        pass
