import unittest

import wardle_py.models as models


class TestCaseStart(unittest.TestCase):

    def test_AnswerStringToString(self):
        answer_string = models.AnswerString("react");
        self.assertEqual(answer_string.toString() , "react")

