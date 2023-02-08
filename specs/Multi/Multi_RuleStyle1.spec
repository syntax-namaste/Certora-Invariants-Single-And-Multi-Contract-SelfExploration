// This spec file is to verify that if we do it in "rule-style",
// it works perfectly fine.

using Second as sec

methods {
    sec.getValueSecond() returns(uint256) envfree;
}

rule arbitRule(env e, uint256 x) {
    require sec.getValueSecond() == 52;
    changeValue(e, x);
    assert sec.getValueSecond() == 52, "valueSecond changed!";
}

// Verification Report: https://prover.certora.com/output/52228/64bd7eee37cf42f6a461d0429951947b?anonymousKey=17c2e17c9a0c896efbe00d35773edbcb6e0c3cf1