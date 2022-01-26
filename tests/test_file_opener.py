import unittest

class UnitTestCase(unittest.TestCase):
    
    def test_file_opener(self):
        self.assertEqual('foo'.upper(), 'FOO')
