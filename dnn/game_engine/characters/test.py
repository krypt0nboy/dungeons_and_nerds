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

    def test_character_demotion(self):
        self.character.rank = 1
        self.character_controller.demote()
        self.assertEqual(self.character.rank, 0)

    def test_character_demotion_below_zero(self):
        with self.assertRaises(CharacterRankUpgradeBelowZeroException):
            self.character_controller.demote()
            self.assertEqual(self.character.rank, 0)

    def test_character_promotion(self):
        self.character_controller.promote()
        self.assertEqual(self.character.rank, 1)

    def tearDown(self):
        pass
