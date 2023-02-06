// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Simple {
    uint256 value1 = 2;
    uint256 value2 = 5;

    // changing value1 inside constructor
    constructor() {
        value1 = 52;
    }

    // changing value2 inside a function
    function someRandomFn() external {
        value2 = 25;
    }
    
    function getValue1() external view returns(uint256) {
        return value1;
    }

    function getValue2() external view returns(uint256) {
        return value2;
    }

}