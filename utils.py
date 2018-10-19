import hashlib


def calc_hash(index, timestamp, data, previous_hash):
    """Implements the hahs function for the blocks."""
    code = str(index) + str(timestamp) + data + previous_hash
    h = hashlib.sha256(code).hexdigest()
    return h