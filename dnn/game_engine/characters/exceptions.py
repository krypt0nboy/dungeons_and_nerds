"""This file provides with character related exceptions.

"""


# __all__ = ['CharacterUpgradeException']

class CharacterException(Exception):
    """
    """
    pass


class CharacterUpgradeException(CharacterException):
    """
    """
    pass


class CharacterDowngradeException(CharacterException):
    """
    """
    pass


class CharacterPointDistributionException(CharacterException):
    """
    """
    pass


class CharacterSkillDoesNotExistException(CharacterPointDistributionException):
    """
    """
    pass


class CharacterPointDistributionIsInactiveException(CharacterException):
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
