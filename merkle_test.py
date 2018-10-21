import unittest
from merkle import Merkle


class TestMerkle(unittest.TestCase):
    def setUp(self):
        self.tree = Merkle()

    def test_block_inits_correctly(self):
        tree = self.tree

        tree.add_leaf("0")
        tree.add_leaf("1")
        self.assertEqual(len(tree), 2)
        tree.add_leaf("2")
        self.assertEqual(len(tree), 3)
        r1 = tree.get_root()
        tree.add_leaf("3")
        self.assertEqual(len(tree), 3)
        r2 = tree.get_root()
        self.assertNotEqual(r1, r2)
        tree.add_leaf("4")
        tree.add_leaf("5")
        tree.add_leaf("6")
        tree.add_leaf("7")
        tree.add_leaf("8")
        self.assertEqual(len(tree), 6)


if __name__ == '__main__':
    unittest.main()
