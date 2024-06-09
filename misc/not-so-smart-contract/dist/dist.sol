// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract challenge {
    address public owner;
    string private flag = "REDACTED";

    constructor() {
        owner = 0xB7981fd3D77498A5c4cFdA7335BE5842F02894eb;
    }

    function getFlag() public view returns (string memory) {
        require(msg.sender == owner, "you aren't the owner!!");
        return flag;
    }

    receive() external payable {}
}