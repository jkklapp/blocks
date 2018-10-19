from time import time
from utils import calc_hash


class Block(object):
    """Represents a valid block."""
    def __init__(self, index, data, previous_hash):
        """Builds a block calculating its hash from he previous one."""
        self.index = index
        self.timestamp = int(time() * 100000)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(self.index, self.timestamp, self.data,
                              self.previous_hash)
