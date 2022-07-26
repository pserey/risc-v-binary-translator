def _rname(reg_add):
    return f'x{int(reg_add, 2)}'


def format_R(conteudos):
    inst = ''
    # exceções no funct7
    if conteudos['funct7'] == '0100000':
        if conteudos['opcode'] == '0010011': inst = 'srai'
        elif conteudos['funct3'] == '000': inst = 'sub'
        elif conteudos['funct3'] == '101': inst = 'sra'
    elif conteudos['opcode'] == '010011':
        if conteudos['funct3'] == '001': inst = 'slli'
        elif conteudos['funct3'] == '101': inst = 'srli'
    else:
        match conteudos['funct3']:
            case '000': inst = 'add'
            case '001': inst = 'sll'
            case '010': inst = 'slt'
            case '011': inst = 'sltu'
            case '100': inst = 'xor'
            case '101': inst = 'srl'
            case '110': inst = 'or'
            case '111': inst = 'and'

    return f"{inst} {_rname(conteudos['rd'])}, {_rname(conteudos['rs1'])}, {_rname(conteudos['rs2'])}"


def format_I(conteudos):
    inst = ''
    # logica imediata?
    if (len(conteudos) == 5):
        if conteudos['opcode'] == '0010011':
            match conteudos['funct3']:
                case '000': inst = 'addi'
                case '010': inst = 'slti'
                case '011': inst = 'sltiu'
                case '100': inst = 'xori'
                case '110': inst = 'ori'
                case '111': inst = 'andi'
        # load?
        elif conteudos['opcode'] == '0000011':
            match conteudos['funct3']:
                case '000': inst = 'lb'
                case '001': inst = 'lh'
                case '010': inst = 'lw'
                case '100': inst = 'lbu'
                case '101': inst = 'lhu'
    else:
        if conteudos['funct3'] == '001': inst = 'slli'
        elif conteudos['funct7'] == '0100000': inst = 'srai'
        else: inst = 'srli'

    return f"{inst} {_rname(conteudos['rd'])}, {_rname(conteudos['rs1'])}, {conteudos['imm']}"

def calc_imm(conteudos):
    cycle = int(conteudos['imm_cycle_32'], 2)
    imm = int(conteudos['imm_offset'], 2)

    return imm + (cycle * 32)


def format_SB(conteudos):
    inst = ''
    match conteudos['funct3']:
        case '000': inst = 'beq'
        case '001': inst = 'bne'
        case '100': inst = 'blt'
        case '101': inst = 'bge'
        case '110': inst = 'bltu'
        case '111': inst = 'bgeu'

    return f"{inst} {_rname(conteudos['rs2'])}, {calc_imm(conteudos)}({_rname(conteudos['rs1'])})"


def format_S(conteudos):
    inst = ''
    match conteudos['funct3']:
        case '000': inst = 'sb'
        case '001': inst = 'sh'
        case '010': inst = 'sw'

    return f"{inst} {_rname(conteudos['rs2'])}, {calc_imm(conteudos)}({_rname(conteudos['rs1'])})"