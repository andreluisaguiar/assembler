import unittest

from parser import Parser


def collect(parser):
    instructions = []

    while parser.hasMoreInstructions():
        instructions.append(parser.advance())

    return instructions


class ParserTest(unittest.TestCase):
    def test_loads_add_asm_without_comments_or_blank_lines(self):
        parser = Parser("projects/06/add/Add.asm")

        self.assertEqual(
            collect(parser),
            [
                "@2",
                "D=A",
                "@3",
                "D=D+A",
                "@0",
                "M=D",
            ],
        )

    def test_has_more_instructions_and_advance_reach_end(self):
        parser = Parser("projects/06/add/Add.asm")

        self.assertTrue(parser.hasMoreInstructions())
        self.assertEqual(parser.advance(), "@2")
        self.assertEqual(parser.current_instruction, "@2")

        while parser.hasMoreInstructions():
            parser.advance()

        self.assertFalse(parser.hasMoreInstructions())
        self.assertIsNone(parser.advance())

    def test_instruction_type_for_a_c_and_label_instructions(self):
        parser = Parser("projects/06/max/Max.asm")

        seen_types = set()

        while parser.hasMoreInstructions():
            parser.advance()
            seen_types.add(parser.instructionType())

        self.assertIn(Parser.A_INSTRUCTION, seen_types)
        self.assertIn(Parser.C_INSTRUCTION, seen_types)
        self.assertIn(Parser.L_INSTRUCTION, seen_types)

    def test_symbol_returns_a_instruction_symbol_and_label_symbol(self):
        parser = Parser("projects/06/max/Max.asm")

        symbols = []

        while parser.hasMoreInstructions():
            parser.advance()

            if parser.instructionType() in (Parser.A_INSTRUCTION, Parser.L_INSTRUCTION):
                symbols.append(parser.symbol())

        self.assertIn("ITSR0", symbols)
        self.assertIn("OUTPUT_D", symbols)
        self.assertIn("END", symbols)
        self.assertIn("R0", symbols)

    def test_dest_comp_and_jump_for_c_instructions(self):
        parser = Parser("projects/06/max/MaxL.asm")
        parsed_c_instructions = []

        while parser.hasMoreInstructions():
            parser.advance()

            if parser.instructionType() == Parser.C_INSTRUCTION:
                parsed_c_instructions.append((parser.dest(), parser.comp(), parser.jump()))

        self.assertIn(("D", "M", None), parsed_c_instructions)
        self.assertIn(("D", "D-M", None), parsed_c_instructions)
        self.assertIn((None, "D", "JGT"), parsed_c_instructions)
        self.assertIn(("M", "D", None), parsed_c_instructions)
        self.assertIn((None, "0", "JMP"), parsed_c_instructions)


if __name__ == "__main__":
    unittest.main()
