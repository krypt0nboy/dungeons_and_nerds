"""This file provides with fight related events.

"""
from dnn.game_engine.events import EventBase


class FightEventBase(EventBase):
    """
    """

    def __init__(self, fight=None):
        self.fight = fight


class FightIsGonnaStartEvent(FightEventBase):
    """
    """
    pass


class FightHasStartedEvent(FightEventBase):
    """
    """
    pass


class FightHasEndedEvent(FightEventBase):
    """
    """
    pass
