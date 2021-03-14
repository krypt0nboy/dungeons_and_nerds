"""This file provides with fight action classes.

A fight action stores a player's action for a given FightTurn.
"""


class FightAction(object):
    """
    """

    def __init__(self, turn=None):
        self._turn = turn


class Attack(FightAction):
    """
    """
    pass


class Defense(FightAction):
    """
    """
    pass
