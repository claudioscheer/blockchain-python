from lib.hash import get_hash_sha1
import binascii, json, os


def bytes_to_hex(bytes):
    return binascii.hexlify(bytes).decode()


def json_to_dict(file):
    if not os.path.isfile(file):
        return {}
    with open(file) as json_file:
        return json.load(json_file)


def dict_to_json(dict):
    return json.dumps(dict)


def save_file_json(file, dict):
    with open(file, "w") as json_file:
        json_file.write(dict_to_json(dict))


def get_block_hash(block):
    return get_hash_sha1(block["prev"] + block["data"] + str(block["nounce"]) +
                         block["name"])
