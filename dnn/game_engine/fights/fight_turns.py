"""This file provides with Fight turn classes.

"""
from datetime import datetime


class FightTurn(object):
    """
    """

    def __init__(self, fight=None, player_1=None, player_2=None, active_player=None, instance_datetime=None,
                 start_datetime=None, end_datetime=None,
                 **kwargs):
        """
        :param fight: The fight for which this turn was instanciated.
        :param active_player: The active player.
        :param instance_datetime: The date and time the turn was instanciated.
        :param start_datetime: The date and time the turn actually started.
        :param end_datetime: The date and time the turn ended.
        :param kwargs:
        """
        self._fight = fight
        self._player_1 = player_1
        self._player_2 = player_2
        self._active_player = active_player
        self._instance_datetime = instance_datetime or datetime.now()
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._actions = []

    @property
    def fight(self):
        return self._fight

    @property
    def player_1(self):
        return self._player_1

    @property
    def player_2(self):
        return self._player_2

    @property
    def active_player(self):
        return self._active_player

    @property
    def instance_datetime(self):
        return self._instance_datetime

    @property
    def start_datetime(self):
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        return self._end_datetime

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, action):
        self._actions.append(action)
