import unittest

import wordle_py as wd
import wordle_py.models as md


class TestCaseWordle(unittest.TestCase):

    def setUp(self):
        self.wordle = wd.wordle.WordleOriginal()
        self.wordle.setAnswer("roast")

    def test_CheckTurn(self):
        i = 0
        answer = md.AnswerStringEnglish('hello')
        while self.wordle.getTurn():
            self.wordle.checkString(answer)
            i += 1
        self.assertEqual(6, i)
        return

