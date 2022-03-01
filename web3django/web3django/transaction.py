from eth_account import Account
from eth_utils import to_wei
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x89BD3b8f3F390330998CEbA250b9665B00EcDfE1"
account_2 = "0x0b39DCB2C6b7A0D1e3c61adB11bEd765b0b5Ce50"

private_key = "552e21c508e08128d58d200b6062efc656fd4256517714ca1f295214675ba442"

nonce = web3.eth.getTransactionCount(account_1)

# build transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# get transaction hash
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
