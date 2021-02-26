"""This file provides with character related event subscribers.

"""


def fight_has_ended(event):
    winner = event.fight._winner
    winner_cc = winner._active_character_controller
    winner_cc.post_fight__as_winner(fight=event.fight)

    loser = event.fight._loser
    loser_cc = loser._active_character_controller
    loser_cc.post_fight__as_loser(fight=event.fight)


def fight_has_started(event):
    """
    :param event:
    :return:
    """
    pass
