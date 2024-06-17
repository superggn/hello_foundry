from eth_account import Account

# demo 1
full_message = {
    "types": {
        "EIP712Domain": [
            {"name": "name", "type": "string"},
            {"name": "version", "type": "string"},
            {"name": "chainId", "type": "uint256"},
            {"name": "verifyingContract", "type": "address"},
        ],
        "Permit": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"},
            {"name": "value", "type": "uint256"},
            {"name": "nonce", "type": "uint256"},
            {"name": "deadline", "type": "uint256"},
        ],
    },
    "primaryType": "Permit",
    "domain": {
        # todo 这个 name 是合约初始化时设定的 name
        "name": "WTFPermit",
        "version": "1",
        "chainId": "1",
        # todo 每次部署都要改
        "verifyingContract": "0xaa7c5414F0b9a6f047640D82D99a1E37387D2BF4",
    },
    "message": {
        "owner": "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",
        "spender": "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2",
        "value": 100,
        "nonce": 0,
        "deadline": 1718607680,
    },
}
key = "0x503f38a9c967ed597e47fe25643985f032b072db8075426a92110f82df48dfcb"
signed_message = Account.sign_typed_data(key, full_message=full_message)
hex(signed_message.r)
hex(signed_message.s)
hex(signed_message.v)

