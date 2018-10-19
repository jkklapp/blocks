import unittest
from block import Block
from utils import calc_hash_with_pow


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(0, 'test', "0")

    def test_block_inits_correctly(self):
        block = self.block
        self.assertEqual(0, block.index)
        self.assertEqual('test', block.data)
        self.assertTrue(len(block.previous_hash), 64)
        self.assertNotEqual(block.previous_hash, block.hash)
        print block

if __name__ == '__main__':
    unittest.main()
