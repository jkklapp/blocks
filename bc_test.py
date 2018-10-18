import unittest

from bc import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.bc = Block(0, 'test', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08')

    def test_block_inits_correctly(self):
        bc = self.bc
        self.assertEqual(0, bc.index)
        self.assertEqual('test', bc.data)
        self.assertTrue(len(bc.previous_hash), 64)


if __name__ == '__main__':
    unittest.main()