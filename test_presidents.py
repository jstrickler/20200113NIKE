#!/usr/bin/env python
import sys
import unittest
from president import President

class TestPresident(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.potus = President(1)


    def test_pres_1_first_name_is_george(self):
        self.assertEqual("George", self.potus.first_name, "First name is not George")

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented in Windows")
    def test_pres_2_first_name_is_washington(self):
        self.assertEqual("Washington", self.potus.last_name, "Last name is not Washington")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=11)
