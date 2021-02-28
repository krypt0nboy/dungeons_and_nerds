import unittest

from dnn.game_engine.characters.characters import CharacterBase
from dnn.game_engine.characters.exceptions import *
from dnn.game_engine.characters.controllers import CharacterController


class CharacterTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        self.character = CharacterBase(base_hp=0, base_dp=0, base_ap=0, base_mp=0, sp=12, rank=0)
        self.character_controller = CharacterController(character=self.character)

    def test_demotion(self):
        self.character.rank = 1
        self.character_controller.demote()
        self.assertEqual(self.character.rank, 1)

    def test_demotion_below_one(self):
        self.character.rank = 1
        self.character_controller.demote()
        self.assertEqual(self.character.rank, 1)

    def test_promotion(self):
        self.character_controller.promote()
        self.assertEqual(self.character.rank, 1)

    def test_sp_distribution(self):
        self.character_controller.init_skill_point_distribution()
        self.character_controller.upgrade_skill(skill='base_hp')
        self.character_controller.end_skill_point_distribution()
        self.assertEqual(self.character.base_hp, 1)
        self.assertEqual(self.character.hp, 1)
        self.assertEqual(self.character.sp, 11)

    def test_sp_distribution_bypassing_init(self):
        with self.assertRaises(CharacterPointDistributionIsInactiveException):
            self.character_controller.upgrade_skill(skill='base_hp')

    def test_sp_distribution_skill_does_not_exist(self):
        with self.assertRaises(CharacterSkillDoesNotExistException):
            self.character_controller.init_skill_point_distribution()
            self.character_controller.upgrade_skill(skill='some_fake_skill')

    def tearDown(self):
        pass
