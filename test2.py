import unittest
import shortrandom_game

class TestGame(unittest.TestCase):
    def test_generator_rightguess(self):
        result = shortrandom_game.generator(5, 5)
        self.assertTrue(result)

    def test_generator_wrongguess(self):
        result = shortrandom_game.generator(2, 5)
        self.assertFalse(result)

    def test_generator_not_between(self):
        result = shortrandom_game.generator(0, 5)
        self.assertFalse(result)

    def test_generator_string(self):
        result = shortrandom_game.generator('11', 5)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()