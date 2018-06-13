#!/usr/bin/env python3
from lib.utils import json_to_dict
from lib.hash import get_hash_sha1

BLOCKCHAIN_FILE_NAME = "blockchain.json"


def get_first_block(blockchain):
    for key, value in blockchain.items():
        if value["prev"] == "genesis":
            return key, value


def get_last_block(blockchain):
    prevs = [o["prev"] for o in blockchain.values()]
    for key, value in blockchain.items():
        if not key in prevs:
            return key, value


def verify_blockchain(blockchain, last_key, last_value):
    prev_key = last_value["prev"]
    if get_hash_sha1(prev_key + last_value["data"]) != last_key:
        return False, last_key, last_value
    if prev_key == "genesis":
        return True, True, True
    return verify_blockchain(blockchain, prev_key, blockchain[prev_key])


if __name__ == "__main__":
    blockchain = json_to_dict(BLOCKCHAIN_FILE_NAME)
    last_key, last_value = get_last_block(blockchain)
    blockchain_valid, error_key, error_block = verify_blockchain(
        blockchain, last_key, last_value)
    if not blockchain_valid:
        print(error_key, error_block)
    print(blockchain_valid)
