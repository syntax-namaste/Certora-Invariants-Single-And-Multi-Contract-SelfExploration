// This spec file highlights the fact that since 'First.sol' inherits from 
// 'Second.sol', we need not use the "using" keyword, making the code simpler.

methods {
    getValueSecond() returns(uint256) envfree;
}

// will pass
rule arbitRule(env e, uint256 x) {
    require getValueSecond() == 52;
    changeValue(e, x);
    assert getValueSecond() == 52, "valueSecond changed!";
}

// Verification Report: https://prover.certora.com/output/52228/25353503d75449d5baceecf9d9f137fe?anonymousKey=6f4e4ba29592fe1b8ac89f2999aa9f4bb2c18b54