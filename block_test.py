import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        previous_hash = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c\
                        15b0f00a08'
        self.bc = Block(0, 'test', previous_hash)

    def test_block_inits_correctly(self):
        bc = self.bc
        self.assertEqual(0, bc.index)
        self.assertEqual('test', bc.data)
        self.assertTrue(len(bc.previous_hash), 64)
        self.assertNotEqual(bc.previous_hash, bc.hash)


if __name__ == '__main__':
    unittest.main()