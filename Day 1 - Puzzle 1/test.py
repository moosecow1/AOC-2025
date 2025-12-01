from main import parseInstruction

assert parseInstruction("L10") == (False, 10)
assert parseInstruction("L1") == (False, 1)
assert parseInstruction("R10") == (True, 10)
assert parseInstruction("R1") == (True, 1)