# instruções de branch
def decode_SB(instruction):
    imm_cycle_32 = instruction[0:7]
    rs2 = instruction[7:12]
    rs1 = instruction[12:17]
    funct3 = instruction[17:20]
    # offset do branch
    imm_offset = instruction[20:25]
    opcode = instruction[25:]

    return imm_cycle_32, rs2, rs1, funct3, imm_offset, opcode


# instruções de load ou lógicas imediatas
def decode_I(instruction):
    # pode ser offset em load ou constante em lógicas
    imm = instruction[0:12]
    rs1 = instruction[12:17]
    funct3 = instruction[17:20]
    rd = instruction[20:25]
    opcode = instruction[25:]

    return imm, rs1, funct3, rd, opcode


# instruções de store
def decode_S(instruction):
    imm_cycle_32 = instruction[0:7]
    rs2 = instruction[7:12]
    rs1 = instruction[12:17]
    funct3 = instruction[17:20]
    imm_offset = instruction[20:25]
    opcode = instruction[25:]

    return imm_cycle_32, rs2, rs1, funct3, imm_offset, opcode


# instruções de shift e não imediatas
def decode_R(instruction):
    funct7 = instruction[0:7]
    rs2 = instruction[7:12]
    rs1 = instruction[12:17]
    funct3 = instruction[17:20]
    rd = instruction[20:25]
    opcode = instruction[25:]

    return funct7, rs2, rs1, funct3, rd, opcode


# simplesmente jal.
def decode_UJ(instruction):
    imm = instruction[0:20]
    rd = instruction[20:25]


# LUI e AUIPC
def decode_U(instruction):
    imm = instruction[0:20]
    rd = instruction[20:25]