"""This file provides with Player base classes.

"""

__all__ = ['PlayerBase']


class PlayerBase(object):
    """
    Base class for Player.
    """

    def __init__(self, username=None, active_character=None, active_character_controller=None):
        """
        :param str username: The player's username.
        :param active_character: The player's active (selected) character.
        :param active_character_controller: The player's active character controller.
        """
        self._username = username
        self._active_character = active_character
        self._active_character_controller = active_character_controller

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def active_character(self):
        return self._active_character

    @property
    def active_character_controller(self):
        return self._active_character_controller

    def select_character(self, character=None):
        pass
