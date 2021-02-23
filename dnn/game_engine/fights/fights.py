"""This file provides with FightBase classes.

"""


class FightBase(object):
    """
    """

    def __init__(self, player_1=None, player_2=None, start_time=None):
        """
        :param player_1: Always the player that started the fight.
        The player that first entered the lobby is the player who started the fight.
        :param player_2:
        :param start_time:
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.start_time = start_time
