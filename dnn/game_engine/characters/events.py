"""This file provides with characters related events.

"""
from dnn.game_engine.events import EventBase


class CharacterEvent(EventBase):
    """
    The base class for Character events.
    """

    def __init__(self, character=None):
        self._character = character

    @property
    def character(self):
        return self._character


class CharacterHasBeenPromotedEvent(CharacterEvent):
    """
    An event that occurs after promoting a character.
    """
    pass


class CharacterHasBeenDemotedEvent(CharacterEvent):
    """
    An event that occurs after demoting a character.
    """
    pass


class CharacterIsGonnaUpgradeSkills(CharacterEvent):
    """
    An event that occurs before a character upgrades his skills.
    """
    pass


class CharacterHasUpgradedSkills(CharacterEvent):
    """
    An event that occurs after a character has upgraded his skills.
    """
    pass


class CharacterHasBeenLockedEvent(CharacterEvent):
    """
    An event that occurs after a character has been locked.
    """

    def __init__(self, lock=None, **kwargs):
        super(CharacterHasBeenLockedEvent, self).__init__(**kwargs)
        self._lock = lock

    @property
    def lock(self):
        return self._lock
