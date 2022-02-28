import unittest

import wordle_py as wd


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wordleOriginal = wd.wordle.WordleOriginal()

    def test_originalClass(self):
        self.wordleOriginal.setAnswer('reset')

    def tearDown(self):
        del self.wordleOriginal
