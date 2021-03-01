"""This file provides with Characters related base classes.

"""
import re

from dnn.game_engine.characters.attributes import *
from dnn.game_engine.characters.locks import *
from dnn.game_engine.characters.controllers import *
from dnn.game_engine.fights.fights import *
from dnn.game_engine.players.players import PlayerBase


class Meta(object):
    """
    Stores meta information for Character class.
    """

    def __init__(self):
        self._skills = {}
        self._attributes = {}


class CharacterMeta(type):
    """
    Metaclass for Character.
    """

    def __new__(mcs, name, bases, attrs):
        if name.startswith('None'):
            return None

        new_attributes = {'meta': Meta()}
        for attr_name, attr_value in attrs.items():
            if not re.match(u'__\w+__', attr_name):
                if isinstance(attr_value, (CharacterAttributeBasedSkill, CharacterAttributeBaseSkill)):
                    new_attributes['meta']._skills[attr_name] = attr_value
                    new_attributes['meta']._attributes[attr_name] = attr_value
                    new_attributes[attr_name] = None
                elif isinstance(attr_value, (CharacterAttribute, CharacterAttributeStat, CharacterAttributeLiveStat)):
                    new_attributes['meta']._attributes[attr_name] = attr_value
                    new_attributes[attr_name] = None
                # TODO handle CharacterAttributeBasedSkill separately to allow skill generic processing in controller
                else:
                    new_attributes[attr_name] = attr_value
            else:
                new_attributes[attr_name] = attr_value

        return super(CharacterMeta, mcs).__new__(mcs, name, bases, new_attributes)


class CharacterBase(object, metaclass=CharacterMeta):
    """
    Base class for character.
    """

    name = CharacterAttribute(name='name', label='Name')
    owner = CharacterAttribute(name='owner', label='Owner')
    base_hp = CharacterAttributeBaseSkill(name='base_health_points', label='Base health points', default=10)
    base_ap = CharacterAttributeBaseSkill(name='base_attack_points', label='Base attack points')
    base_mp = CharacterAttributeBaseSkill(name='base_magik_points', label='Base magik points')
    base_dp = CharacterAttributeBaseSkill(name='base_defense_points', label='Base defense points')
    hp = CharacterAttributeBasedSkill(name='health_points', label='Health points', base_skill=base_hp, default=10)
    ap = CharacterAttributeBasedSkill(name='attack_points', label='Attack points', base_skill=base_ap)
    mp = CharacterAttributeBasedSkill(name='magik_points', label='Magik points', base_skill=base_mp)
    dp = CharacterAttributeBasedSkill(name='defense_points', label='Defense points', base_skill=base_dp)
    sp = CharacterAttributeLiveStat(name='skill_points', label='Skill points', default=12)
    rank = CharacterAttributeLiveStat(name='rank', label='Rank', default=1)
    is_locked = CharacterAttributeLiveStat(name='is_locked', label='Is locked')
    lock = CharacterAttributeLiveStat(name='lock', label='Lock')
    last_fight = CharacterAttributeLogStat(name='last_fight', label='Last fight')
    num_victories = CharacterAttributePerfStat(name='num_victories', label='Number of victories')
    num_defeats = CharacterAttributePerfStat(name='num_defeats', label='Number of defeats')
    num_flawless_victories = CharacterAttributePerfStat(name='num_flawless_victories',
                                                        label='Number of flawless victories')

    def __init__(self, **kwargs):
        for attr_name, attr in self.meta._attributes.items():
            if attr_name in kwargs.keys():
                setattr(self, attr_name, kwargs.pop(attr_name))
            elif attr.default is not None:
                setattr(self, attr_name, attr.default)

    def get_skill_level(self, skill: str = None):
        return getattr(self, skill)

    def set_skill_level(self, skill: str = None, level: int = None):
        return setattr(self, skill, level)

    @classmethod
    def controller_base_class(cls):
        return CharacterControllerBase
