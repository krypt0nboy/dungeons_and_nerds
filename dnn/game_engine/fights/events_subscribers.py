"""This file provides with fight related event subscribers.

"""


def character_health_is_zero_or_less(character=None):
    """
    :param character:
    :return:
    """
    fight = character.player.current_fight
    fight.set_loser(character.player)
