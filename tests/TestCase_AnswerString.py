import unittest

import wardle_py.models as models


class TestCaseStart(unittest.TestCase):

    def test_AnswerStringToString(self):
        answer_string = models.AnswerStringEnglish("react");
        self.assertEqual("react", answer_string.toString())

