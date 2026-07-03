from enum import Enum
from pathlib import Path


class InstructionType(str, Enum):
    A_INSTRUCTION = "A_INSTRUCTION"
    C_INSTRUCTION = "C_INSTRUCTION"
    L_INSTRUCTION = "L_INSTRUCTION"


class Parser:
    """Parser for Hack assembly files."""

    A_INSTRUCTION = InstructionType.A_INSTRUCTION.value
    C_INSTRUCTION = InstructionType.C_INSTRUCTION.value
    L_INSTRUCTION = InstructionType.L_INSTRUCTION.value

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.instructions = self._load_instructions()
        self.current_index = -1
        self.current_instruction = None

    def _load_instructions(self):
        instructions = []

        with self.file_path.open("r", encoding="utf-8") as source:
            for line in source:
                instruction = line.split("//", 1)[0].strip()

                if instruction:
                    instructions.append("".join(instruction.split()))

        return instructions

    def hasMoreInstructions(self):
        return self.current_index + 1 < len(self.instructions)

    def advance(self):
        if not self.hasMoreInstructions():
            self.current_instruction = None
            return None

        self.current_index += 1
        self.current_instruction = self.instructions[self.current_index]
        return self.current_instruction

    def instructionType(self):
        self._ensure_current_instruction()

        if self.current_instruction.startswith("@"):
            return self.A_INSTRUCTION

        if self.current_instruction.startswith("(") and self.current_instruction.endswith(")"):
            return self.L_INSTRUCTION

        return self.C_INSTRUCTION

    def symbol(self):
        instruction_type = self.instructionType()

        if instruction_type == self.A_INSTRUCTION:
            return self.current_instruction[1:]

        if instruction_type == self.L_INSTRUCTION:
            return self.current_instruction[1:-1]

        raise ValueError("symbol() is valid only for A or label instructions")

    def dest(self):
        self._ensure_c_instruction()

        if "=" not in self.current_instruction:
            return None

        return self.current_instruction.split("=", 1)[0]

    def comp(self):
        self._ensure_c_instruction()

        instruction = self.current_instruction

        if "=" in instruction:
            instruction = instruction.split("=", 1)[1]

        if ";" in instruction:
            instruction = instruction.split(";", 1)[0]

        return instruction

    def jump(self):
        self._ensure_c_instruction()

        if ";" not in self.current_instruction:
            return None

        return self.current_instruction.split(";", 1)[1]

    def reset(self):
        self.current_index = -1
        self.current_instruction = None

    def _ensure_current_instruction(self):
        if self.current_instruction is None:
            raise ValueError("No current instruction. Call advance() first.")

    def _ensure_c_instruction(self):
        if self.instructionType() != self.C_INSTRUCTION:
            raise ValueError("This method is valid only for C instructions")
