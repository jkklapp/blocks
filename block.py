from utils import calc_hash
from utils import get_block_timestamp
from datetime import datetime


class Block(object):
    """Represents a valid block."""
    def __init__(self, index, data, previous_hash):
        """Builds a block calculating its hash from he previous one."""
        self.index = index
        self.timestamp = get_block_timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(self.index, self.timestamp, str(self.data),
                              self.previous_hash)

    def __repr__(self):
        t = self.timestamp / 10000
        return "Block:" + str(self.index) + ":" + \
            datetime.fromtimestamp(t).strftime("%d/%m/%Y %H:%M:%S") + \
            ":" + str(self.data) + ":" + self.hash
