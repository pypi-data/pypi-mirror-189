import json
import requests
from web3 import Web3
from eth_account.messages import encode_defunct
from .utils import decode_raw_tx


class madz:
    def __init__(self, node="https://78.58.45.205"):
        self.node = node
        self.w3node = node + "/web3"
        self.w3 = Web3(Web3.HTTPProvider(self.w3node))

    def _check(self):
        if not self.w3.isConnected():
            self.w3 = Web3(Web3.HTTPProvider(self.w3node)) #if not connected to node, perform a reconnect
            if not self.w3.isConnected():
                raise ConnectionError
            else:
                return
        else:
            return

    def sign_transaction(self, private_key, transaction):
        message = encode_defunct(text=transaction["data"])
        transaction["hash"] = self.w3.soliditySha3(["string"], [transaction["data"]]).hex()
        _signature = self.w3.eth.account.sign_message(message, private_key=private_key).signature.hex()
        signer = self.w3.eth.account.recover_message(message, signature=_signature)
        sender = self.w3.toChecksumAddress(json.loads(transaction["data"])["from"])
        if (signer == sender):
            transaction["sig"] = _signature
        return transaction

    def get_last_transaction(self, address):
        """Get last transaction of a user."""
        self._check()
        r = requests.get(f"{self.node}/accounts/accountInfo/{address}")
        return r.json()["result"]["transactions"][len(r.json()["result"]["transactions"]) - 1]

    def get_epoch(self):
        """"Get current block."""
        self._check()
        r = requests.get(f"{self.node}/chain/getlastblock").json()["result"]["miningData"]["proof"]
        return r

    def transaction(self, privkey, fromaddr, to, amount, additional_data={}):
        """Build a transaction and send it to the node. Returns ``False`` or the txid."""
        self._check()
        try:
            address = self.w3.eth.account.privateKeyToAccount(privkey).address
            if address != fromaddr:
                raise ValueError(f"Private key does not match address. (Private key is for {address})")
        except:
            raise ValueError("Invalid private key")
        try:
            fromaddr = self.w3.toChecksumAddress(fromaddr)
            to = self.w3.toChecksumAddress(to)
            data = {"from": fromaddr, "to": to, "tokens": amount, "parent": self.get_last_transaction(fromaddr), "epoch": self.get_epoch(), "type": 0}
            data.update(additional_data)
            strdata = json.dumps(data)
            tx = {"data": strdata}
            signature = self.sign_transaction(privkey, tx)
            a = json.dumps(signature)
            a = a.encode().hex()
            r = requests.get(f"{self.node}/send/rawtransaction/?tx={a}")
            if r.json()["success"] == True:
                return r.json()["result"][0]
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def balance(self, address):
        """Get balance of a user."""
        self._check()
        return requests.get(f"{self.node}/accounts/accountBalance/{address}").json()["result"]["balance"]
    
    def get_tx(self, txid):
        """Get transaction by id. Returns `(data, type, hash, sig)`"""
        if not self.is_txid(txid):
            raise ValueError("Not a TX")
        r = requests.get(f"{self.node}/get/transaction/{txid}").json()
        if not r["success"]:
            return False
        r = r["result"]
        data = r["data"]

        data = json.loads(data)

        if data["type"] == 0:
            hash = r["hash"]
            sig = r["sig"]
            data.pop("type")
            type = 0

        elif data["type"] == 1:
            hash = r["hash"]
            sig = r["sig"]
            data.pop("type")
            type = 1
        
        elif data["type"] == 2:
            hash = None
            sig = r["sig"]
            data.pop("type")
            type = 2
            data = decode_raw_tx(data["rawTx"])



        return data, type, hash, sig 
