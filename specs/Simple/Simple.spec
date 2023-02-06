methods {
    getValue1() returns uint256 envfree;
    getValue2() returns uint256 envfree;
}

// will pass, as constructor call is not 
// considered by rules
rule rule_value1_is_constant(method f, env e) {
    require getValue1() == 2;
    calldataarg args;
    f(e, args);
    assert getValue1() == 2, "value1 changed";
}

// will fail, as value2 was changed by 
// a function named someRandomFn()
rule rule_value2_is_constant(method f, env e) {
    require getValue2() == 5;
    calldataarg args;
    f(e, args);
    assert getValue2() == 5, "value2 changed";
}

// will fail, as invariant checks the
// condition after making a constructor call too.
// Failure reason would be:
// invariant_value1_is_constant_instate --> invariant violated in post-state
invariant invariant_value1_is_constant()
    getValue1() == 2

// will fail, as value2 was modified in a function.
// Failure reason would be:
// invariant_value2_is_constant_preserve --> someRandomFn() --> invariant violated in post-state
invariant invariant_value2_is_constant()
    getValue2() == 5

// will pass, since using 'requireInvariant' is just a
// fancy way of writing 'require', and because we're inside a rule, 
// the constructor is not called
rule rule_with_invariant_value1_is_constant(method f, env e) {
    requireInvariant invariant_value1_is_constant();
    calldataarg args;
    f(e, args);
    assert getValue1() == 2, "value1 changed";
}    

// Verification Report: https://prover.certora.com/output/52228/11f14299f4934cdb828fefaea851c84e