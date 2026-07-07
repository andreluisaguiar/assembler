import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "code"))
from code.code import encode_a_instruction, encode_c_instruction

class CodeTest(unittest.TestCase):
    def test_instrucao(self):
        self.assertEqual(encode_a_instruction(0), "0000000000000000")
        self.assertEqual(encode_a_instruction(2), "0000000000000010")
        self.assertEqual(encode_a_instruction(16), "0000000000010000")

    def test_instrucao_completa(self):
        self.assertEqual(encode_c_instruction("D+A", "D", "JMP"), "1110000010010111")
        
    def test_instrucao_defaults(self):
        self.assertEqual(encode_c_instruction("A", "D", None), "1110110000010000")
        self.assertEqual(encode_c_instruction("0", None, "JMP"), "1110101010000111")

if __name__ == "__main__":
    unittest.main()