#!/usr/bin/python3

from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.sepolia.org'))

contract_address = '0xC95AB4E8BD3820E8cea0d4B5b5aB628168Aab0b7'

contract = web3.eth.contract(address=contract_address)


def read_storage():
    flag_position = 1
    storage_value = web3.eth.get_storage_at(contract_address, flag_position)
    print("Stored value: ", storage_value.hex())


read_storage()
