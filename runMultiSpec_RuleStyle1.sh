solc-select use 0.8.0

certoraRun contracts/Multi/First.sol contracts/Multi/Second.sol \
--verify First:specs/Multi/Multi_RuleStyle1.spec \
--solc solc \
--msg "Multi_Invariant_Spec_RuleStyle1"