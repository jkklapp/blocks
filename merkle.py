from utils import calc_hash_for_two_hashes


class Merkle(object):
    def __init__(self):
        self.data = []

    def add_leaf(self, t):
        if not self.data:
            self.data.append([])
        l = len(self.data)
        if len(self.data[l-1]) < 2:
            self.data[l-1].append(t)
        else:
            self.data.append([t])
        r = self.compute_root()
        if len(self.data) >= 2:
            self.data.pop(0)
        self.data.insert(0, r)

    def get_root(self):
        return self.data[0]

    def compute_root(self):
        h_list = []
        data = self.data
        if len(data) > 1:
            data = data[1:]

        for i in range(0, len(data)):
            h_list += data[i]
            if len(data[i]) == 1:
                h_list += data[i]  # Insert twice if leaf is single

        l = len(h_list)

        while l > 1:
            a = h_list[l-1]
            b = h_list[l-2]
            h_list = h_list[:-2]
            h = calc_hash_for_two_hashes(a, b)
            h_list.insert(0, h)
            l = len(h_list)

        return h_list[0]

    def __repr__(self):
        return "Tree:Root:" + str(self.data[0]) + ':Leaves:' + str(self.data[1:])

    def __len__(self):
        return len(self.data)