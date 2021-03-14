"""This file provides with FightBase classes.

"""
import random
from datetime import datetime

import zope.event

from dnn.game_engine.fights.events import *
from dnn.game_engine.fights.fight_turns import FightTurn


class FightBase(object):
    """
    """

    def __init__(self, player_1=None, player_2=None, start_datetime=None, end_datetime=None, loser=None, winner=None,
                 turns=None, fight_is_over=False):
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
        self._players = [player_1, player_2]
        self._start_datetime = start_datetime or datetime.now()
        self._end_datetime = end_datetime
        self._current_active_player = player_1
        self._loser = loser
        self._winner = winner
        self._turns = turns or []
        self._current_turn = None
        self._fight_is_over = fight_is_over

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

    @property
    def turns(self):
        return self._turns

    @turns.setter
    def turns(self, turn):
        self._turns.append(turn)

    @property
    def current_turn(self):
        return self._current_turn

    @current_turn.setter
    def current_turn(self, turn):
        self._current_turn = turn

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
        """
        Instanciates a new turn.
        :return: The instanciated turn
        :rtype: FightTurn
        """
        if not self._fight_is_over:
            turn = FightTurn(fight=self, player_1=self.player_1, player_2=self.player_2,
                             active_player=self.guess_turn_active_player())
            self.current_turn = turn
            self.turns = turn

    def guess_turn_active_player(self):
        """
        :return: dnn.game_engine.players.players.PlayerBase
        """
        if not len(self._turns):
            return self._player_1
        else:
            return [self._player_1, self._player_2][random.randint(0, 1)]

    def start_turn(self):
        self.current_turn.start_datetime = datetime.now()

    def end_turn(self):
        pass

    def set_loser(self, player=None):
        self._fight_is_over = True
        tmp_players = self._players
        tmp_players.pop(player)
        self._loser = player

    def process_attack_and_defense(self):
        pass
