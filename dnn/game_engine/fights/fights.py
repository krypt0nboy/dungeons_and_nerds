"""This file provides with FightBase classes.

"""
from datetime import datetime

import zope.event

from dnn.game_engine.fights.events import *


class FightBase(object):
    """
    """

    def __init__(self, player_1=None, player_2=None, start_datetime=None, end_datetime=None, loser=None, winner=None,
                 turns=None):
        """
        :param player_1: Always the player that started the fight.
        The player that first entered the lobby is the player who started the fight.
        :param player_2: The player 2.
        :param start_datetime: The date and time the fight started.
        :param end_datetime: The date and time the fight ended.
        :param loser: The loser of the fight.
        :param winner: The winner of the fight.
        :param turns: The fight turns.
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self._start_datetime = start_datetime or datetime.now()
        self._end_datetime = end_datetime
        self._current_active_player = player_1
        self._loser = loser
        self._winner = winner
        self._turns = turns or []

    @property
    def player_1(self):
        """
        :rtype: dnn.game_engine.players.players.PlayerBase
        """
        return self._player_1

    @property
    def player_2(self):
        """
        :rtype: dnn.game_engine.players.players.PlayerBase
        """
        return self._player_2

    @property
    def start_datetime(self):
        return self._start_datetime

    @property
    def end_datetime(self):
        return self._end_datetime

    @property
    def current_active_player(self):
        """
        :rtype: dnn.game_engine.players.players.PlayerBase
        """
        return self._current_active_player

    @property
    def loser(self):
        """
        :rtype: dnn.game_engine.players.players.PlayerBase
        """
        return self._loser

    @property
    def winner(self):
        """
        :rtype: dnn.game_engine.players.players.PlayerBase
        """
        return self._winner

    def prepare_fight(self):
        """
        :return:
        """
        event = FightIsGonnaStartEvent(fight=self)
        zope.event.notify(event)

    def start_fight(self):
        """
        :return:
        """
        event = FightHasStartedEvent(fight=self)
        zope.event.notify(event)

    def end_fight(self):
        """
        :return:
        """
        event = FightHasEndedEvent(fight=self)
        zope.event.notify(event)

    def new_turn(self):
        pass

    def start_turn(self):
        pass

    def end_turn(self):
        pass
