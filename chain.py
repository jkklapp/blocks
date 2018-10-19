from block import Block


class Chain(object):
    """Makes easier to handle blocks."""
    def __init__(self):
        self.data = []

    def first(self):
        """Generate beginning of the chain."""

        block = Block(0, "First block", "0")  # with hash = 0
        self.data.append(block)
        return block

    def next(self, previous, data):
        """Compute the next block using the previous one."""

        block = Block(previous.index + 1, data, previous.hash)
        self.data.append(block)
        return block
