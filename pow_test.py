import unittest
from utils import calc_hash_with_pow


class TestCalculateHashWithPOW(unittest.TestCase):
    """Test POW hash calc."""
    def setUp(self):
        self.h = calc_hash_with_pow(0, "test", "0", "0")

    def test_hash_is_valid(self):
        self.assertTrue(self.h.startswith("0"))

if __name__ == '__main__':
    unittest.main()
