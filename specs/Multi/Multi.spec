using Second as sec

methods {
    sec.getValueSecond() returns(uint256) envfree;
}

// will fail, as constructors of contracts other than the
// 'currentContract' are not invoked by invariants
invariant valueSecond_is_constant()
    sec.getValueSecond() == 52

// will pass, for the same reasons as above
invariant valueSecond_is_zero()
    sec.getValueSecond() == 0

// will pass, as 'requireInvariant' is just a 'require'
rule arbitRule(env e, uint256 x) {
    requireInvariant valueSecond_is_constant();
    changeValue(e, x);
    assert sec.getValueSecond() == 52, "valueSecond changed!";
}

// Verification Report: https://prover.certora.com/output/52228/df239cab650546d5b6642b45793a5e62