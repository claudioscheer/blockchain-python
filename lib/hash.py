from Crypto.Hash import SHA


def get_hash_sha1(data):
    h = SHA.new()
    h.update(data.encode("utf-8"))
    return h.hexdigest()
