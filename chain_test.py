"""
Test chain module.
"""
import unittest
from chain import Chain


class TestChain(unittest.TestCase):
    """Test basic chain functionality."""
    def setUp(self):
        self.chain = Chain()
        self.first = self.chain.first()

    def test_chain_get_first(self):
        first = self.first
        self.assertEqual(0, first.index)
        self.assertEqual('First block', first.data)
        self.assertEqual("0", first.previous_hash)
        self.assertTrue(len(first.previous_hash), 1)
        self.assertNotEqual(first.previous_hash, first.hash)

    def test_chain_get_next(self):
        first = self.first
        second = self.chain.next(first, "Second block")
        self.assertEqual(first.index + 1, second.index)
        self.assertEqual(second.data, "Second block")

    def test_chain_three_block(self):
        first = self.first
        tA = {
            'from': 'user1', 'to': 'user2', 'item': 'token', 'q': 10
        }
        tB = {
            'from': 'user3', 'to': 'user5', 'item': 'token', 'q': 7
        }
        tC = {
            'from': 'user0', 'to': 'user15', 'item': 'token', 'q': 3
        }
        second = self.chain.next(first, tA)
        third = self.chain.next(second, tB)
        fourth = self.chain.next(third, tC)
        # print first, second, third, fourth
        self.assertIsNotNone(fourth)


if __name__ == '__main__':
    unittest.main()
