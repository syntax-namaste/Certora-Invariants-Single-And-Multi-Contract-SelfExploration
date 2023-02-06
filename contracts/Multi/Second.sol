// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Second {
    uint256 valueSecond;

    constructor() {
        valueSecond = 52;
    }

    function getValueSecond() external view returns(uint256) {
        return valueSecond;
    }
}