import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from parser.parser import Parser, InstructionType
from symbol_table.symbol_table import SymbolTable
from code.code import encode_a_instruction, encode_c_instruction

def assemble(file_path: str):
    path = Path(file_path)
    parser = Parser(path)
    symbol_table = SymbolTable()
    
    rom_address = 0
    while parser.hasMoreInstructions():
        parser.advance()
        ins_type = parser.instructionType()
        
        if ins_type == InstructionType.L_INSTRUCTION.value:
            label = parser.symbol()
            symbol_table.addEntry(label, rom_address)
        else:
            rom_address += 1
   
    parser.reset()
    binary_instructions = []
   
    while parser.hasMoreInstructions():
        parser.advance()
        ins_type = parser.instructionType()
        
        if ins_type == InstructionType.A_INSTRUCTION.value:
            symbol = parser.symbol()
            
            if symbol.isdigit():
                address = int(symbol)
            else:
                if symbol_table.contains(symbol):
                    address = symbol_table.getAddress(symbol)
                else:
                    address = symbol_table.addVariable(symbol)
                    
            binary_instructions.append(encode_a_instruction(address))
            
        elif ins_type == InstructionType.C_INSTRUCTION.value:
            comp = parser.comp()
            dest = parser.dest()
            jump = parser.jump()
            binary_instructions.append(encode_c_instruction(comp, dest, jump))

    output_dir = Path("out")
    output_dir.mkdir(exist_ok=True) 

    output_path = output_dir / path.with_suffix(".hack").name  
    with output_path.open("w", encoding="utf-8") as out_file:
        out_file.write("\n".join(binary_instructions) + "\n")
        
    print(f"Sucesso: Arquivo gerado em em '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main/assembler.py <caminho_do_arquivo.asm>")
    else:
        assemble(sys.argv[1])

