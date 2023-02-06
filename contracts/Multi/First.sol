// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;
import "./Second.sol";

contract First is Second {
    uint256 valueFirst;

    function changeValue(uint256 valueX) external {
        valueFirst = valueX + valueSecond;
    }
}
