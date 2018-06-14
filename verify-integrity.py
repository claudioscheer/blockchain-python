#!/usr/bin/env python3
from lib.utils import json_to_dict, get_block_hash

BLOCKCHAIN_FILE_NAME = "blockchain.json"


def get_last_block(blockchain):
    prevs = [o["prev"] for o in blockchain.values()]
    for key, value in blockchain.items():
        if not key in prevs:
            return key, value


def verify_blockchain(blockchain, last_key, last_value):
    prev_key = last_value["prev"]
    if get_block_hash(last_value) != last_key:
        return False, last_key, last_value
    if last_key == "0000090a504e11e4a0d062c81f41a3628f03c31c":
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
