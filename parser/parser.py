from pathlib import Path


class Parser:
    """Parser for Hack assembly files."""

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
