"""This file provides with characters related events.

"""
from dnn.game_engine.events import EventBase


class CharacterEvent(EventBase):
    """
    The base class for Character events.
    """
    pass


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
