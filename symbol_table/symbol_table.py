class SymbolTable:
    """Stores Hack symbols and their numeric RAM or ROM addresses."""

    def __init__(self):
        self.table = self._predefined_symbols()
        self.next_variable_address = 16

    def addEntry(self, symbol, address):
        self.table[symbol] = int(address)

    def addVariable(self, symbol):
        if not self.contains(symbol):
            self.addEntry(symbol, self.next_variable_address)
            self.next_variable_address += 1

        return self.getAddress(symbol)

    def contains(self, symbol):
        return symbol in self.table

    def getAddress(self, symbol):
        if not self.contains(symbol):
            raise KeyError(f"Symbol not found: {symbol}")

        return self.table[symbol]

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
