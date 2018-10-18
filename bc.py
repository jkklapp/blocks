import hashlib
import datetime
from random import random

class Block(object):
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        code = str(self.index) + \
               str(self.timestamp) + \
               self.data + self.previous_hash
        h = hashlib.sha256(code).hexdigest()
        return h
