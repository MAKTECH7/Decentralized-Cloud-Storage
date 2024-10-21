from blockchain import Blockchain  # Import the Blockchain class from your blockchain.py file

blockchain = Blockchain()  # Initialize the blockchain

# Create a sample metadata object
metadata = {'filename': 'test_file.txt', 'hash': 'some_hash'}

# Add the metadata to the blockchain
blockchain.create_block(metadata, blockchain.get_previous_block()['hash'])

# Print the blockchain to see if the block is added
print(blockchain.chain)
