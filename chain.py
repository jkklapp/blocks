from block import Block


class Chain(object):
    """Makes easier to handle blocks."""
    def first(self):
        """Generate beginning of the chain."""
        return Block(0, "First block", "0")  # with hash = 0 

    def next(self, previous, data):
        """Compute the next block using the previous one."""
        return Block(previous.index + 1, data, previous.hash)