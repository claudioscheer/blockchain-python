#!/usr/bin/env python3
from lib.utils import json_to_dict, save_file_json
from lib.hash import get_hash_sha1

BLOCKCHAIN_FILE_NAME = "blockchain.json"


def get_blockchain():
    return {}


def create_init_block():
    block = {"prev": "genesis", "data": "singularity"}
    return get_hash_sha1(block["prev"] + block["data"]), block


if __name__ == "__main__":
    blockchain = get_blockchain()
    h, block = create_init_block()
    blockchain[h] = block
    save_file_json(BLOCKCHAIN_FILE_NAME, blockchain)
