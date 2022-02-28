import unittest

import wordle_py as wd
import wordle_py.models as md


class TestCaseWordle(unittest.TestCase):

    def test_CheckTurn(self):
        self.wordle = wd.wordle.WordleOriginal()
        self.wordle.setAnswer("roast")
        i = 0
        answer = md.AnswerStringEnglish('hello')
        while self.wordle.getTurn():
            self.wordle.checkString(answer)
            i += 1
        self.assertEqual(6, i)
        return

    def test_CheckString(self):
        self.wordle = wd.wordle.WordleOriginal()
        self.wordle.setAnswer("roast")
        answer = md.AnswerStringEnglish('roast')
        self.assertListEqual([2, 2, 2, 2, 2], self.wordle.checkString(answer))

    def test_CheckString2(self):
        self.wordle = wd.wordle.WordleOriginal()
        self.wordle.setAnswer("roast")
        answer = md.AnswerStringEnglish('bigstring')
        try:
            self.assertListEqual([2, 2, 2, 2, 2], self.wordle.checkString(answer))
        except Exception as e:
            self.assertEqual('Each string is not the same size.', e.__str__())

