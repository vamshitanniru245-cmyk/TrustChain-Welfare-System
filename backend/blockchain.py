from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
print("Connected:", web3.is_connected())

# Replace with your Ganache account
account = web3.eth.accounts[0]

def store_on_blockchain(beneficiary, amount):
    tx = {
        'from': account,
        'to': account,
        'value': web3.to_wei(0, 'ether'),
        'gas': 2000000,
        'data': web3.to_hex(text=f"{beneficiary}-{amount}")
    }

    tx_hash = web3.eth.send_transaction(tx)
    web3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash.hex()   # 🔥 THIS IS THE KEY CHANGE