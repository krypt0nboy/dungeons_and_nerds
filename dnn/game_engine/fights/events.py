"""This file provides with fight related events.

"""
from dnn.game_engine.events import EventBase


class FightEventBase(EventBase):
    """
    Base class for fight events.
    """

    def __init__(self, fight=None):
        """
        :param fight: The fight for which the event is occurring.
        """
        self.fight = fight


class FightIsGonnaStartEvent(FightEventBase):
    """
    An event that occurs when a fight is about to start.
    """
    pass


class FightHasStartedEvent(FightEventBase):
    """
    An event that occurs when a fight has started.
    """
    pass


class FightHasEndedEvent(FightEventBase):
    """
    An event that occurs when a fight has ended.
    """
    pass
