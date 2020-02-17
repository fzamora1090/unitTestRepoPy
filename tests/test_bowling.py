# test code, test code
# using bolt-ta - Bolt gives you the power to specify how tasks should be executed, and it takes care of the rest. And it is a simple as describing and configuring your tasks in the boltfile.py, 
# nose - unit testing lib
# conttest - continuous testing plugin for nose, 

import unittest

import bowling as bowl

class TestBowlingCalculator(unittest.TestCase):

    def setUp(self):
        self.game = bowl.BowlingGame()

    def test_roll_all_zeros(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_roll_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_roll_all_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 16)

    def test_roll_strike(self):
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 26)

    def test_all_strikes(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def roll_many(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)

    # change public interface in tests then produce code to make the test pass