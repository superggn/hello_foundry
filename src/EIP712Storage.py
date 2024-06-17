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
        "Storage": [
            {"name": "spender", "type": "address"},
            {"name": "number", "type": "uint256"},
        ],
    },
    "primaryType": "Storage",
    "domain": {
        "name": "EIP712Storage",
        "version": "1",
        "chainId": "1",
        # todo 每次部署都要改
        "verifyingContract": "0xaE7A2AB9883E1A4add3900c910F95eB90D31a323",
    },
    "message": {
        "spender": "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",
        "number": 11,
    },
}
key = "0x503f38a9c967ed597e47fe25643985f032b072db8075426a92110f82df48dfcb"
signed_message = Account.sign_typed_data(key, full_message=full_message)
signed_message

