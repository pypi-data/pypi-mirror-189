import rlp
import secrets
from web3.auto import w3
from rlp.sedes import Binary, big_endian_int, binary
from re import search

class Transaction(rlp.Serializable):
    fields = [
        ("nonce", big_endian_int),
        ("gas_price", big_endian_int),
        ("gas", big_endian_int),
        ("to", Binary.fixed_length(20, allow_empty=True)),
        ("value", big_endian_int),
        ("data", binary),
        ("v", big_endian_int),
        ("r", big_endian_int),
        ("s", big_endian_int),
    ]

def decode_raw_tx(raw_tx):
    tx = rlp.decode(bytes.fromhex(raw_tx.replace("0x", "")), Transaction)
    from_ = w3.eth.account.recover_transaction(raw_tx)
    to = w3.toChecksumAddress(tx.to) if tx.to else None
    tokens = w3.fromWei(tx.value, "ether")
    return {"from": from_, "to": to, "tokens": tokens}

def is_address(address):
    """Checks if the address is valid."""
    return w3.isAddress(address)
    
def is_txid(txid):
    """Checks if a transaction hash/ID is valid."""
    return bool(search("^[0-9a-fA-F]{64}$$", txid.replace("0x", "")))

def get_new_address():
    """Returns new address and private key. NEVER SHARE YOUR PRIVATE KEY!"""
    privkey = "0x" + secrets.token_hex(32)
    return w3.eth.account.privateKeyToAccount(privkey).address, privkey

def address_from_private_key(privkey):
    """Returns the address belonging to a private key."""
    return w3.eth.account.privateKeyToAccount(privkey).address
