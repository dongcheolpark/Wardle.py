import unittest

import wordle_py.models as models


class TestCaseAnswerString(unittest.TestCase):

    def test_AnswerStringToString(self):
        answer_string = models.AnswerStringEnglish("react")
        self.assertEqual("react", answer_string.toString())

    def test_AnswerStringIsSame1(self):
        answer_string = models.AnswerStringEnglish("react")
        supposition_string = models.AnswerStringEnglish("roast")
        res = answer_string.CheckString(supposition_string)
        self.assertListEqual(res, [2, 0, 2, 0, 2])

    def test_AnswerStringIsSame2(self):
        answer_string = models.AnswerStringEnglish("react")
        supposition_string = models.AnswerStringEnglish("rcast")
        res = answer_string.CheckString(supposition_string)
        self.assertListEqual(res, [2, 1, 2, 0, 2])

    def test_AnswerStringIsSame3(self):
        answer_string = models.AnswerStringEnglish("reaction")
        supposition_string = models.AnswerStringEnglish("acentric")
        res = answer_string.CheckString(supposition_string)
        self.assertListEqual(res, [1, 1, 1, 1, 2, 1, 1, 1])

    def test_AnswerStringIsSame5(self):
        answer_string = models.AnswerStringEnglish("abcdefg")
        supposition_string = models.AnswerStringEnglish("hijklmn")
        res = answer_string.CheckString(supposition_string)
        self.assertListEqual(res, [0, 0, 0, 0, 0, 0, 0])

    def test_AnswerStringSizeIsDifferent(self):
        answer_string = models.AnswerStringEnglish("abcdefg")
        supposition_string = models.AnswerStringEnglish("hijklmno")
        try:
            res = answer_string.CheckString(supposition_string)
        except Exception as e:
            self.assertEqual('Each string is not the same size.', e.__str__())


class TestCaseAnswerStringFactory(unittest.TestCase):

    def test_AnswerStringGetOriginal(self):
        res = models.AnswerStringFactory().getString('original','roast')
        self.assertEqual('roast', res.toString())
