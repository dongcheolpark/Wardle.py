import unittest

import wardle_py as wd


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wardle = wd.wardle.WardleOriginal()

    def test_is_same_zero(self):
        self.assertEqual(self.wardle.get_answerString().toString(), '')

    def tearDown(self):
        del self.wardle
