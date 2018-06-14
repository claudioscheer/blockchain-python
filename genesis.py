#!/usr/bin/env python3
from lib.utils import json_to_dict, save_file_json, get_block_hash

BLOCKCHAIN_FILE_NAME = "blockchain.json"


def get_blockchain():
    return {}


def create_init_block():
    block = {
        "prev": "genesis",
        "data": "singularity",
        "nounce": 0,
        "name": "claudio"
    }
    nounce = -1
    while 1:
        nounce += 1
        block["nounce"] = nounce
        hash = get_block_hash(block)
        if hash.startswith("00000"):
            return hash, block


if __name__ == "__main__":
    blockchain = get_blockchain()
    h, block = create_init_block()
    blockchain[h] = block
    save_file_json(BLOCKCHAIN_FILE_NAME, blockchain)
