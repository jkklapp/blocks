import unittest
from chain import Chain


class TestChain(unittest.TestCase):
    def setUp(self):
        self.chain = Chain()

    def test_chain_get_first(self):
        first = self.chain.first()
        self.assertEqual(0, first.index)
        self.assertEqual('First block', first.data)
        self.assertEqual("0", first.previous_hash)
        self.assertTrue(len(first.previous_hash), 1)
        self.assertNotEqual(first.previous_hash, first.hash)

    def test_chain_get_next(self):
        first = self.chain.first()
        second = self.chain.next(first, "Second block")
        self.assertEqual(first.index + 1, second.index)
        self.assertEqual(second.data, "Second block")
        

if __name__ == '__main__':
    unittest.main()