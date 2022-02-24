import unittest

from wardle_py.wardle import Wardle


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wardle = Wardle()

    def test_is_same_zero(self):
        self.assertEqual(self.wardle.get_answerString(), '')

    def tearDown(self):
        del self.wardle
