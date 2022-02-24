import unittest

import wordle_py as wd


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wordle = wd.wordle.WordleOriginal()

    def test_is_same_zero(self):
        self.assertEqual(self.wordle.get_answerString().toString(), '')

    def tearDown(self):
        del self.wordle
