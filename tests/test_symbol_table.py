import unittest

from symbol_table import SymbolTable


class SymbolTableTest(unittest.TestCase):
    def test_initializes_predefined_symbols(self):
        table = SymbolTable()

        self.assertEqual(table.getAddress("SP"), 0)
        self.assertEqual(table.getAddress("LCL"), 1)
        self.assertEqual(table.getAddress("ARG"), 2)
        self.assertEqual(table.getAddress("THIS"), 3)
        self.assertEqual(table.getAddress("THAT"), 4)
        self.assertEqual(table.getAddress("SCREEN"), 16384)
        self.assertEqual(table.getAddress("KBD"), 24576)

        for index in range(16):
            self.assertEqual(table.getAddress(f"R{index}"), index)

    def test_add_entry_registers_label_addresses(self):
        table = SymbolTable()

        table.addEntry("LOOP", 4)
        table.addEntry("END", 18)

        self.assertTrue(table.contains("LOOP"))
        self.assertEqual(table.getAddress("LOOP"), 4)
        self.assertEqual(table.getAddress("END"), 18)

    def test_add_variable_allocates_from_address_16(self):
        table = SymbolTable()

        self.assertEqual(table.addVariable("i"), 16)
        self.assertEqual(table.addVariable("sum"), 17)
        self.assertEqual(table.addVariable("i"), 16)
        self.assertEqual(table.getAddress("sum"), 17)

    def test_get_address_raises_for_unknown_symbol(self):
        table = SymbolTable()

        with self.assertRaises(KeyError):
            table.getAddress("UNKNOWN")


if __name__ == "__main__":
    unittest.main()
