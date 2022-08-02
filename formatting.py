import yaml


def _rname(reg_add):
    xname = f'x{int(reg_add, 2)}'
    stream = open('regs.yaml', 'r')
    regs = yaml.load(stream, Loader=yaml.FullLoader)

    return regs[xname]


def calc_imm(conteudos):
    cycle = int(conteudos['imm_cycle_32'], 2)
    imm = int(conteudos['imm_offset'], 2)

    return imm + (cycle * 32)


def format_R(conteudos):
    inst = ''
    stream = open('instructions.yaml', 'r')
    instrucoes = yaml.load(stream, Loader=yaml.FullLoader)

    for dict in instrucoes['R']:
        if conteudos['funct7'] == dict['funct7'] and conteudos['funct3'] == dict['funct3']:
            inst = dict['name']

    return f"{inst} {_rname(conteudos['rd'])}, {_rname(conteudos['rs1'])}, {_rname(conteudos['rs2'])}"


def format_I(conteudos):
    inst = ''
    stream = open('instructions.yaml', 'r')
    instrucoes = yaml.load(stream, Loader=yaml.FullLoader)

    for dict in instrucoes['I']:
        if conteudos['funct3'] == dict['funct3'] and conteudos['opcode'] == dict['opcode']: inst = dict['name']

    # formatação para instruções de logica imediata
    if (len(conteudos) == 5):
        if conteudos['opcode'] == '0010011':
            return f"{inst} {_rname(conteudos['rd'])}, {_rname(conteudos['rs1'])}, {int(conteudos['imm'], 2)}"
        # formatação para instruções de load
        elif conteudos['opcode'] == '0000011':
            return f"{inst} {_rname(conteudos['rd'])}, {conteudos['imm']}({_rname(conteudos['rs1'])})"
    # formatação para instruções de shift
    else:
        return f"{inst} {_rname(conteudos['rd'])}, {_rname(conteudos['rs1'])}, {int(conteudos['shamt'], 2)}"


def format_SB(conteudos):
    inst = ''
    stream = open('instructions.yaml', 'r')
    instrucoes = yaml.load(stream, Loader=yaml.FullLoader)

    for dict in instrucoes['SB']:
        if conteudos['funct3'] == dict['funct3']: inst = dict['name']

    return f"{inst} {_rname(conteudos['rs1'])}, {_rname(conteudos['rs2'])}, {calc_imm(conteudos)}"


def format_S(conteudos):
    inst = ''
    stream = open('instructions.yaml', 'r')
    instrucoes = yaml.load(stream, Loader=yaml.FullLoader)

    for dict in instrucoes['S']:
        if conteudos['funct3'] == dict['funct3']: inst = dict['name']

    return f"{inst} {_rname(conteudos['rs2'])}, {calc_imm(conteudos)}({_rname(conteudos['rs1'])})"