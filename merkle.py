from utils import calc_hash_for_two_hashes


class Merkle(object):
    def __init__(self):
        self.data = []
        self.root = None

    def __repr__(self):
        return "Tree:Root:" + str(self.root) + ':Leaves:' + str(self.data)

    def __len__(self):
        return len(self.data)

    def _compute_root(self):
        data = self.data[:]
        if len(data) % 2 == 0:
            data.append(data[-1])  # Repeat node if length is an odd number

        # Compute intermediate hashes
        while len(data) > 1:
            a = data[len(data)-1]
            b = data[len(data)-2]
            data = data[:-2]
            h = calc_hash_for_two_hashes(a, b)
            data.insert(0, h)

        return data[0]

    def add_leaf(self, t):
        self.data.append(t)
        self.root = self._compute_root()
        print self

    def get_root(self):
        return self.root
