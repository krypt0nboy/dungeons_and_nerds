"""This file provides with character related exceptions.

"""

#__all__ = ['CharacterUpgradeException']


class CharacterUpgradeException(Exception):
    """
    """
    pass


class CharacterDowngradeException(Exception):
    """
    """
    pass


class CharacterSkillUpgradeException(CharacterUpgradeException):
    """
    """
    pass


class CharacterRankUpgradeException(CharacterUpgradeException):
    """
    """
    pass


class CharacterRankDowngradeException(CharacterDowngradeException):
    """
    """
    pass


class CharacterRankUpgradeBelowZeroException(CharacterRankDowngradeException):
    """
    """
    pass
