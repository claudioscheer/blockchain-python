import hashlib


def get_hash_sha1(data):
    hash_object = hashlib.sha1(data.encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    return hex_dig
