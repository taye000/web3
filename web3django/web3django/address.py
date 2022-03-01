# web3 library that contains functions to generate Ethereum accounts and sign transactions and data
from distutils.util import rfc822_escape
from socket import RCVALL_OFF
from eth_account import Account
# python module used for generating random numbers
import secrets

priv = secrets.token_hex(32)
private_key = "0x" + priv
print("SAVE BUT DO NOT SHARE:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)
