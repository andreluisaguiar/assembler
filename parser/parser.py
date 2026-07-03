from pathlib import Path


class Parser:
    """Parser for Hack assembly files."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.instructions = self._load_instructions()

    def _load_instructions(self):
        instructions = []

        with self.file_path.open("r", encoding="utf-8") as source:
            for line in source:
                instruction = line.split("//", 1)[0].strip()

                if instruction:
                    instructions.append("".join(instruction.split()))

        return instructions
