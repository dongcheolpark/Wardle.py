import unittest

import wordle_py.models as models


class TestCaseStart(unittest.TestCase):

    def test_AnswerStringToString(self):
        answer_string = models.AnswerStringEnglish("react")
        self.assertEqual("react", answer_string.toString())

    def test_AnswerStringIsSame1(self):
        answer_string = models.AnswerStringEnglish("react")
        supposition_string = models.AnswerStringEnglish("roast")
        res = answer_string.CheckString(supposition_string)
        self.assertEqual(res, [2, 0, 2, 0, 2])

    def test_AnswerStringIsSame2(self):
        answer_string = models.AnswerStringEnglish("react")
        supposition_string = models.AnswerStringEnglish("rcast")
        res = answer_string.CheckString(supposition_string)
        self.assertEqual(res, [2, 1, 2, 0, 2])

