"""This file provides with FightBase classes.

"""
from datetime import datetime

import zope.event

from dnn.game_engine.fights.events import *


class FightBase(object):
    """
    """

    def __init__(self, player_1=None, player_2=None, start_datetime=None):
        """
        :param player_1: Always the player that started the fight.
        The player that first entered the lobby is the player who started the fight.
        :param player_2:
        :param start_datetime:
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self._start_datetime = start_datetime or datetime.now()
        self._end_datetime = None
        self._current_active_player = player_1
        self._loser = None
        self._winner = None

    def prepare_fight(self):
        pass

    def start_fight(self):
        pass

    def end_fight(self):
        self._winner = self._player_1
        self._loser = self._player_2
        event = FightHasEndedEvent(fight=self)
        zope.event.notify(event)
