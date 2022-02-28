import unittest

import wordle_py as wd


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wordleOriginal = wd.wordle.WordleOriginal()

    def test_originalClass(self):
        self.wordleOriginal.setAnswer('reset')  # 정답 단어 reset으로 정하기

    def tearDown(self):
        del self.wordleOriginal
