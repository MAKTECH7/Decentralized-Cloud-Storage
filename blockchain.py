import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', metadata={})

    def create_block(self, metadata, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'metadata': metadata,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]
