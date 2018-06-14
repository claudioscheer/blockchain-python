#!/usr/bin/env python3
from sys import argv
from lib.utils import json_to_dict, save_file_json, get_block_hash

BLOCKCHAIN_FILE_NAME = "blockchain.json"


def get_blockchain():
    return json_to_dict(BLOCKCHAIN_FILE_NAME)


def get_last_block(blockchain):
    prevs = [o["prev"] for o in blockchain.values()]
    for key, value in blockchain.items():
        if not key in prevs:
            return key, value


def get_block(blockchain, data):
    hash, _ = get_last_block(blockchain)
    block = {"prev": hash, "data": data, "nounce": 0, "name": "claudio"}
    nounce = -1
    while 1:
        nounce += 1
        block["nounce"] = nounce
        hash = get_block_hash(block)
        if hash.startswith("000000"):
            return hash, block


if __name__ == "__main__":
    blockchain = get_blockchain()
    h, block = get_block(blockchain, argv[1])
    blockchain[h] = block
    save_file_json(BLOCKCHAIN_FILE_NAME, blockchain)
