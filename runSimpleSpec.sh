solc-select use 0.8.0

certoraRun contracts/Simple/Simple.sol \
--verify Simple:specs/Simple/Simple.spec \
--solc solc \
--msg "Simple_Invariant_Spec"