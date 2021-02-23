"""This file provides with CharacterAttribute base classes.

"""
import logging

from dnn.game_engine.game_attributes import GameAttributeBase

__all__ = ['CharacterAttributeBase', 'CharacterAttribute', 'CharacterAttributeStat', 'CharacterAttributeLiveStat',
           'CharacterAttributeSkill', 'CharacterAttributeBaseSkill', 'CharacterAttributeBasedSkill',
           'CharacterAttributePerfStat', 'CharacterAttributeLogStat']

logger = logging.getLogger(__name__)


class CharacterAttributeBase(GameAttributeBase):
    """
    """

    def __init__(self, **kwargs):
        super(CharacterAttributeBase, self).__init__(**kwargs)


class CharacterAttribute(CharacterAttributeBase):
    """
    """
    pass


class CharacterAttributeStat(CharacterAttributeBase):
    """
    """
    pass


class CharacterAttributeLiveStat(CharacterAttributeBase):
    """
    """
    pass


class CharacterAttributePerfStat(CharacterAttributeStat):
    """
    """
    pass


class CharacterAttributeLogStat(CharacterAttributeStat):
    """
    """
    pass


class CharacterAttributeSkill(CharacterAttribute):
    """
    """
    pass


class CharacterAttributeBaseSkill(CharacterAttributeSkill):
    """
    """

    def __init__(self, uses_exponential_upgrade: bool = False, based_skill=None,
                 **kwargs):
        """
        :param base_skill:
        :param uses_exponential_upgrade:
        :param kwargs:
        """
        super(CharacterAttributeBaseSkill, self).__init__(**kwargs)
        self._uses_exponential_upgrade = uses_exponential_upgrade
        self._based_skill = based_skill


class CharacterAttributeBasedSkill(CharacterAttributeSkill):
    """
    """

    def __init__(self, base_skill: CharacterAttributeBaseSkill = None,
                 **kwargs):
        """
        :param base_skill:
        :param uses_exponential_upgrade:
        :param kwargs:
        """
        super(CharacterAttributeBasedSkill, self).__init__(**kwargs)
        self._base_skill = base_skill
        self._base_skill._based_skill = self
