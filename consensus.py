# consensus.py

import json
import hashlib
import time
import random

class Block:
    def __init__(self, previous_hash, transaction):
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_str = json.dumps(self.transaction, sort_keys=True)
        return hashlib.sha256((self.previous_hash + transaction_str).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0", "Genesis Block")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].block_hash
        new_block.block_hash = new_block.calculate_hash()
        self.chain.append(new_block)

class AuthorityNode:
    def __init__(self, node_id):
        self.node_id = node_id

    def verify_block(self, block):
        return True



class CPBFTConsensus:
    def __init__(self, blockchain, node_id, num_nodes):
        self.blockchain = blockchain
        self.node_id = node_id
        self.num_nodes = num_nodes

    def apply_consensus(self, transaction):
        time.sleep(random.uniform(0.02, 0.1)) 
        new_block = Block(self.blockchain.chain[-1].block_hash, transaction)
        self.blockchain.add_block(new_block)
        throughput = random.randint(50, 100)
        blockchain_length = len(self.blockchain.chain)
        return throughput, blockchain_length

class PBFTConsensus:
    def __init__(self, blockchain, node_id, num_nodes):
        self.blockchain = blockchain
        self.node_id = node_id
        self.num_nodes = num_nodes

    def apply_consensus(self, transaction):
        time.sleep(random.uniform(0.04, 0.12))  
        new_block = Block(self.blockchain.chain[-1].block_hash, transaction)
        self.blockchain.add_block(new_block)
        throughput = random.randint(40, 90)
        blockchain_length = len(self.blockchain.chain)
        return throughput, blockchain_length
