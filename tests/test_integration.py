import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from main.assembler import assemble

class IntegrationTest(unittest.TestCase):
    def test_assemble_add_and_max(self):
        add_asm = Path("projects/06/add/Add.asm")
        max_asm = Path("projects/06/max/Max.asm")
        
        out_dir = Path("out")
        
        if add_asm.exists():
            assemble(str(add_asm))
            self.assertTrue((out_dir / "Add.hack").exists())
            
        if max_asm.exists():
            assemble(str(max_asm))
            self.assertTrue((out_dir / "Max.hack").exists())

if __name__ == "__main__":
    unittest.main()