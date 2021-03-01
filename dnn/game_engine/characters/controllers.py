"""This file provides with CharacterController base classes.

"""
import logging
import random
from math import ceil

import zope.event

from dnn.game_engine.characters.exceptions import *
from dnn.game_engine.characters.attributes import CharacterAttributeBaseSkill
from dnn.game_engine.characters.events import CharacterHasBeenLockedEvent, CharacterHealthIsZeroOrLess
from dnn.game_engine.characters.utils import lock_character

logger = logging.getLogger(__name__)


class CharacterControllerBase(object):
    """
    Base class for CharacterController.
    """

    def __init__(self, character=None):
        """
        :param dnn.game_engine.characters.characters.CharacterBase character:
        """
        self._character = character


class CharacterController(CharacterControllerBase):
    """
    """

    def __init__(self, **kwargs):
        self._tmp_skill_points = None
        self._tmp_skills = {}
        self._skill_point_distribution_is_active = False
        super(CharacterController, self).__init__(**kwargs)

    def init_skill_point_distribution(self):
        """
        Initializes a skill point distribution.
        During the distribution and until validation, the skill points can be redeemed and reassigned.
        :return: None
        """
        if self.can_init_skill_point_distribution():
            self._skill_point_distribution_is_active = True
            self.init_tmp_skill_points()
            self.init_tmp_skills()
        else:
            raise CharacterUpgradeException("Skill points are already being distributed")

    def can_init_skill_point_distribution(self):
        """
        Checks and indicates if the character controller can init a skill points distribution.
        :return: A boolean indicating if it can init a spd.
        :rtype: bool
        """
        if not self._skill_point_distribution_is_active:
            return True
        else:
            return False

    def init_tmp_skill_points(self):
        """
        Initializes the temporary available skill points based on the character's current skill points.
        :return: None
        """
        if self._skill_point_distribution_is_active:
            self._tmp_skill_points = self._character.sp
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def init_tmp_skills(self):
        """
        Initializes the temporary skills based on the character's current skills levels.
        :return: None
        """
        if self._skill_point_distribution_is_active:
            for skill_name, skill in self._character.meta._skills.items():
                if isinstance(skill, CharacterAttributeBaseSkill):
                    self._tmp_skills[skill_name] = {'level': self._character.get_skill_level(skill_name),
                                                    'skill': skill}
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def end_skill_point_distribution(self):
        """
        Ends a skill point distribution and makes the spended skill points un redeemable.
        :return:
        """
        self.validate_skill_points_distribution()
        self.reset_tmp_skill_points()
        self._skill_point_distribution_is_active = False

    def reset_tmp_skill_points(self):
        """
        Resets the temporary skill points so that the player cannot spend the currently available sp infinitely.
        :return: None
        """
        if self._skill_point_distribution_is_active:
            self._tmp_skill_points = 0

    def validate_skill_points_distribution(self):
        """
        Validates a skill points distribution by updating the character's skill points and skills levels.
        :return: None
        """
        if self._skill_point_distribution_is_active:
            for skill_name, tmp_skill in self._tmp_skills.items():
                self._character.set_skill_level(skill=skill_name, level=tmp_skill['level'])
                self._character.set_skill_level(skill=skill_name.split('_')[1], level=tmp_skill['level'])
            self._character.sp = self._tmp_skill_points
            self._tmp_skills = {}
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def update_based_skills(self):
        """
        Updates the based skills with the base skills as references.
        :return: None
        """
        pass

    def get_tmp_skill_level(self, skill=None):
        if self._skill_point_distribution_is_active:
            return self._tmp_skills[skill]['level']
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def upgrade_skill(self, skill=None):
        """
        Upgrades a character's skill.
        :param str skill: The skill to upgrade.
        :return: The updated skill value.
        :rtype: int
        """
        if self._skill_point_distribution_is_active:
            cost = self.compute_upgrade_cost(skill=skill)
            if self._tmp_skill_points >= cost:
                self._tmp_skills[skill]['level'] = self.get_tmp_skill_level(skill=skill) + 1
                self._tmp_skill_points -= 1
                return self._tmp_skills
            else:
                raise CharacterUpgradeException("No skill points to spend")
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def compute_upgrade_cost(self, skill=None):
        """
        Computes the skill points cost to upgrade a skill.
        :param str skill: The skill for which to compute the upgrade cost.
        :return: The cost.
        :rtype: int
        """
        if self._skill_point_distribution_is_active:
            if skill in self._tmp_skills.keys():
                if self._tmp_skills[skill]['skill']._uses_exponential_upgrade:
                    return ceil(self.get_tmp_skill_level(skill=skill) / 5)
                else:
                    return 1
            else:
                raise CharacterSkillDoesNotExistException("No such skill as %s" % skill)
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def downgrade_skill(self, skill=None):
        """
        Downgrades a character's skill.
        :param skill: The skill to downgrade.
        :return: The updated skill value.
        :rtype: int
        """
        if self._skill_point_distribution_is_active:
            current_tmp_skill_level = self.get_tmp_skill_level(skill=skill)
            if current_tmp_skill_level >= 1:
                credit = self.compute_downgrade_credit(skill=skill)
                if credit:
                    self._tmp_skills[skill] = current_tmp_skill_level - 1
                    self._tmp_skill_points += 1
                    return self._tmp_skill_points
            else:
                raise CharacterUpgradeException("Skill cannot be downgraded further")
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def compute_downgrade_credit(self, skill=None):
        """
        Computes the skill points credit for a skill downgrade.
        :param str skill: The skill for which to compute the downgrade credit.
        :return: The credit.
        :rtype: int
        """
        if self._skill_point_distribution_is_active:
            current_skill_level = self._character.get_skill_level(skill=skill)
            if current_skill_level >= 1:
                if self._tmp_skills[skill]['skill']._uses_exponential_upgrade:
                    return ceil((current_skill_level - 1) / 5)
                else:
                    return 1
        else:
            raise CharacterPointDistributionIsInactiveException("Skill distribution must be active")

    def promote(self):
        """
        Promotes a character (Rank up).
        :return: The updated character's rank.
        :rtype: int
        """
        self._character.rank += 1
        return self._character.rank

    def demote(self):
        """
        Demotes a character (Rank down).
        :return: The updated characters's rank.
        :rtype: int
        """
        if self._character.rank > 1:
            self._character.rank -= 1
            return self._character.rank
        # else:
        # raise CharacterDemotionBelowOneException("Character cannot be demoted further")

    def lock(self, **kwargs):
        """
        Locks a character and makes it unavailable until the lock is destroyed.
        :param kwargs:
        :return:
        """
        character_lock = lock_character(character=self)
        if character_lock:
            event = CharacterHasBeenLockedEvent(character=self, lock=character_lock)
            zope.event.notify(event)

    def unlock(self, **kwargs):
        """
        Unlocks a character and destroys any active lock.
        :param kwargs:
        :return:
        """
        pass

    def increase_health(self, amount=None):
        """
        Increases the character's health by the provided amount.
        :param amount: The amount of health to add.
        :return: The character's updated health points.
        :rtype: int
        """
        self._character.hp += amount
        return self._character.hp

    def decrease_health(self, amount=None):
        """
        Decreases the character's health by the provided amount.
        :param amount: The amount of health to remove.
        :return: The character's updated health points.
        :rtype: int
        """
        self._character.hp -= amount
        if self._character.hp <= 0:
            zope.event.notify(CharacterHealthIsZeroOrLess)
        return self._character.hp

    def replenish_health(self):
        """
        Replenishes the character's health.
        :return: The character's updated health points.
        :rtype: int
        """
        self._character.hp = self._character.base_hp
        return self._character.hp

    def roll_attack_dice(self):
        return random.randint(0, self._character.ap)

    def roll_magik_dice(self):
        return random.randint(0, self._character.mp)

    def post_fight(self, fight=None):
        """
        Run required routines after a fight.
        :param fight: The fight for which to run the post routines.
        :return: None
        """
        pass

    def post_fight__as_winner(self, fight=None):
        """
        Runs post fight routines after winning a fight.
        :param fight:
        :return:
        """
        self.promote()
        self.replenish_health()

    def post_fight__as_loser(self, fight=None):
        """
        Runs post fight routines after losing a fight.
        :param fight:
        :return:
        """
        self.demote()
        self.lock()


class CharacterCombatController(CharacterControllerBase):
    """
    """

    def __init__(self, fight=None, **kwargs):
        super(CharacterCombatController, self).__init__(**kwargs)
