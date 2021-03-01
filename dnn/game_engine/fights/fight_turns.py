"""This file provides with Fight turn classes.

"""


class FightTurn(object):
    """
    """

    def __init__(self, fight=None, active_player=None, instance_datetime=None, start_datetime=None, end_datetime=None,
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
        self._active_player = active_player
        self._instance_datetime = instance_datetime
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._actions = []

    @property
    def fight(self):
        return self._fight

    @property
    def active_player(self):
        return self._active_player

    @property
    def instance_datetime(self):
        return self._instance_datetime

    @property
    def start_datetime(self):
        return self._start_datetime

    @property
    def end_datetime(self):
        return self._end_datetime
