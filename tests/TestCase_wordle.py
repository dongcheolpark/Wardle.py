import unittest

import wordle_py as wd
import wordle_py.models as md


class TestCaseWordle(unittest.TestCase):

    def test_CheckTurn(self):
        wordle = wd.wordle.WordleOriginal()
        wordle.setAnswer("roast")
        i = 0
        answer = md.AnswerStringEnglish('hello')
        while wordle.getTurn():
            wordle.checkString(answer)
            i += 1
        self.assertEqual(6, i)
        return

    def test_SetAnswerRandom(self):
        wordle = wd.wordle.WordleOriginal()
        wordle.setAnswer()
        ans = wordle.answer_String
        self.assertNotEqual([], ans)

    def test_CheckString(self):
        wordle = wd.wordle.WordleOriginal()
        wordle.setAnswer("roast")
        answer = md.AnswerStringEnglish('roast')
        self.assertListEqual([2, 2, 2, 2, 2], wordle.checkString(answer))

    def test_CheckString2(self):
        wordle = wd.wordle.WordleOriginal()
        wordle.setAnswer("roast")
        answer = md.AnswerStringEnglish('bigstring')
        try:
            self.assertListEqual([2, 2, 2, 2, 2], wordle.checkString(answer))
        except Exception as e:
            self.assertEqual('Each string is not the same size.', e.__str__())

    def test_CheckStringInAnswerList(self):
        wordle = wd.wordle.WordleOriginal()
        wordle.setAnswer("roast")
        answer = md.AnswerStringEnglish('rando') # List에 없는 단어
        self.assertEqual(False, wordle.checkString(answer, inDictionary=true))


