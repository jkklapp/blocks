import hashlib
from time import time


def calc_hash(index, timestamp, data, previous_hash):
    """Implements the hahs function for the blocks."""
    code = str(index) + str(timestamp) + data + previous_hash
    h = hashlib.sha256(code).hexdigest()
    return h


def calc_hash_for_two_hashes(a, b):
    """Implements the hahs function for the blocks."""
    h = hashlib.sha256(a + b).hexdigest()
    return h


def calc_hash_with_pow(index, data, previous_hash, difficulty="00"):
    found = False
    while found is False:
        timestamp = get_block_timestamp()
        h = calc_hash(index, timestamp, data, previous_hash)
        if h.startswith(difficulty):
            found = True

    return h


def get_block_timestamp():
    return int(time() * 10000)
