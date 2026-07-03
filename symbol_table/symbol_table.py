class SymbolTable:
    """Stores Hack symbols and their numeric RAM or ROM addresses."""

    def __init__(self):
        self.table = self._predefined_symbols()

    @staticmethod
    def _predefined_symbols():
        symbols = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
        }

        for index in range(16):
            symbols[f"R{index}"] = index

        return symbols
