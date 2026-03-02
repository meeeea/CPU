import sys

opcodes = {
    "NOP" : "0", "LD" : "1", "MV" : "2", "DISP" : "3", "XOR" : "4",
    "AND" : "5", "OR" : "6", "ADD" : "7", "XNOR" : "8", "NAND" : "9",
    "NOR" : "a", "SUB" : "f", "WRT" : "b"
}

write_Op_set = ["3","b"]
standard_Op_set = ["4","5","6","7","8","9","a","f"]

def main(args):
    with open(args[1], mode="r") as file:
        lines = file.readlines()
        if lines:
            with open(args[2], mode="w") as target:
                target.write("v3.0 hex words plain\n")
                column = 0
                for line in lines:
                    if column == 7:
                        target.write("\n")
                        column = 0

                    opcode = line.split()[0]
                    writen = opcodes[opcode]
                    match writen:
                        case "1":
                            write_address, data = line.split()[1:]
                            writen += hex(int(write_address.strip("Rr,"))).strip("0x").rjust(2,"0")
                            writen += hex(int(data)).strip("0x").rjust(8,"0")
                            target.write(f"{writen} ")
                            column += 1
                        case "2":
                            WAddr, RAddr = line.split()[1:]
                            writen += hex(int(WAddr.strip("Rr,"))).strip("0x").rjust(2,"0")
                            writen += hex(int(RAddr.strip("Rr,"))).strip("0x").rjust(8,"0")
                            target.write(f"{writen} ")
                            column += 1
                        case Opcode if Opcode in write_Op_set:
                            RAddr = line.split()[1]
                            writen += hex(int(WAddr.strip("Rr,"))).strip("0x").rjust(10,"0")
                            target.write(f"{writen} ")
                            column += 1
                        case Opcode if Opcode in standard_Op_set:
                            WAddr, RAddr_A, RAddr_B = line.split()[1:]
                            writen += hex(int(WAddr.strip("Rr,"))).strip("0x").rjust(2,"0")
                            writen += hex(int(RAddr_B.strip("Rr,"))).strip("0x").rjust(6,"0")
                            writen += hex(int(RAddr_A.strip("Rr,"))).strip("0x").rjust(2,"0")
                            target.write(f"{writen} ")
                            column += 1


main(sys.argv)