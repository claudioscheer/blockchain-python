#!/usr/bin/env python3
from sys import argv
from lib.utils import json_to_dict, save_file_json
from lib.hash import get_hash_sha1

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
    block = {"prev": hash, "data": data}
    return get_hash_sha1(block["prev"] + block["data"]), block


if __name__ == "__main__":
    blockchain = get_blockchain()
    h, block = get_block(blockchain, argv[1])
    blockchain[h] = block
    save_file_json(BLOCKCHAIN_FILE_NAME, blockchain)
