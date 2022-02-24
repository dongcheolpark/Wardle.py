import unittest

import wardle_py as wd


class TestCaseStart(unittest.TestCase):

    def setUp(self):
        self.wardle = wd.models.Wardle()
        
    def test_is_same_zero(self):
        self.assertEqual(self.wardle.get_answerString(), '')

    def tearDown(self):
        del self.wardle
