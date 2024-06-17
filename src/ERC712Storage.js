const domain = {
    name: "EIP712Storage",
    version: "1",
    chainId: "1",
    verifyingContract: "0xaE7A2AB9883E1A4add3900c910F95eB90D31a323",
};
const types = {
    Storage: [
        { name: "spender", type: "address" },
        { name: "number", type: "uint256" },
    ],
};

const message = {
    spender: "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",
    number: "11",
};


const { ethers } = await import("ethers");


const privateKey = '0x503f38a9c967ed597e47fe25643985f032b072db8075426a92110f82df48dfcb';

// Create a new Wallet instance using the private key
const wallet = new ethers.Wallet(privateKey);

signed_data = wallet.signTypedData(domain, types, message)

// 0xa977be5daeb5aafbd5625fd9e03793f7b6ae71f1b0b8d3c156a01704b3d8982e7812e8bd6c68be65d9dada55d3ac10ef7b6428227648f3ba13c388460528ad7d1b

