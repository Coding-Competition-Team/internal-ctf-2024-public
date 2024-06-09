# not-so-smart-contract

Author: Sean 3

**Difficulty: Medium**

## Description

The IPC has made a smart contract to keep secrets! (and pay your taxes!!!)

Contract: 0xC95AB4E8BD3820E8cea0d4B5b5aB628168Aab0b7

Network: Sepolia testnet

## Solution

In solidity, 'private' variables mean that it cannot be accessed or modified from from other smart contracts, not that it is hidden or obfuscated in anyway.

```js
    address public owner;
    string private flag = "REDACTED";
```

Since the flag is the second variable to be created after the owner address, which is 20 bytes, we can deduce that the flag will be stored in slot 0 if it is 12 bytes or less, or slot 1 if it is more than 12 bytes 

We can write a script using the web3 module in python to solve this

```py
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.sepolia.org'))

contract_address = '0xC95AB4E8BD3820E8cea0d4B5b5aB628168Aab0b7'

contract = web3.eth.contract(address=contract_address)


def read_storage():
    flag_position = 1
    storage_value = web3.eth.get_storage_at(contract_address, flag_position)
    print("Stored value: ", storage_value.hex())


read_storage()
```

This outputs `0x414353497b44754d425f63304e745261432b5f66663630336233657d00000038`, which when converted from hex to ascii, is the flag `ACSI{DuMB_c0NtRaC+_ff603b3e}`.
