"""This file provides with character related exceptions.

"""


# __all__ = ['CharacterUpgradeException']


class CharacterUpgradeException(Exception):
    """
    """
    pass


class CharacterDowngradeException(Exception):
    """
    """
    pass


class CharacterPointDistributionException(Exception):
    """
    """
    pass


class CharacterSkillDoesNotExistException(CharacterPointDistributionException):
    """
    """
    pass


class CharacterPointDistributionIsInactiveException(Exception):
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


class CharacterDemotionException(CharacterDowngradeException):
    """
    """
    pass


class CharacterDemotionBelowOneException(CharacterDemotionException):
    """
    """
    pass
