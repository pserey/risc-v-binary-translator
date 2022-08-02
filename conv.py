from decoding import *
from formatting import *


def inst_type(instruction):
    formato = ''
    opcode = instruction[25:len(instruction) + 1]

    if opcode == '1101111': formato = 'UJ'
    elif opcode == '1100011': formato = 'SB'
    elif opcode == '0100011': formato = 'S'
    elif opcode == '0110111' or opcode == '0010111': formato = 'U'
    elif opcode == '0000011' or opcode == '1100111' or opcode == '0010011': formato = 'I'
    elif opcode == '0110011': formato = 'R'

    return formato


def inst_decode(instruction):
    formato = inst_type(instruction)

    match formato:
        case 'R':
            conteudos = {}
            conteudos['funct7'], conteudos['rs2'], conteudos['rs1'], conteudos['funct3'], conteudos['rd'], conteudos['opcode'] = decode_R(instruction)

            return format_R(conteudos)
        case 'SB':
            conteudos = {}
            conteudos['imm_cycle_32'], conteudos['rs2'], conteudos['rs1'], conteudos['funct3'], conteudos['imm_offset'], conteudos['opcode'] = decode_SB(instruction)

            return format_SB(conteudos)
        case 'S':
            conteudos = {}
            conteudos['imm_cycle_32'], conteudos['rs2'], conteudos['rs1'], conteudos['funct3'], conteudos['imm_offset'], conteudos['opcode'] = decode_S(instruction)

            return format_S(conteudos)
        case 'I':
            imm, rs1, funct3, rd, opcode = decode_I(instruction)
            conteudos = {}
            # se é 001 ou 101 então é shift lógico e portanto tem formatação diferente
            if ((opcode == '0010011' and (funct3 != '001' and funct3 != '101')) or opcode == '0000011'):
                conteudos['imm'] = imm
                conteudos['rs1'] = rs1
                conteudos['funct3'] = funct3
                conteudos['rd'] = rd
                conteudos['opcode'] = opcode
            # shift lógicos tem a formatação de instruções R
            # shamt = shift amount
            else:
                funct7, shamt, rs1, funct3, rd, opcode = decode_R(instruction)
                conteudos['funct7'] = funct7
                conteudos['shamt'] = shamt
                conteudos['rs1'] = rs1
                conteudos['funct3'] = funct3
                conteudos['rd'] = rd
                conteudos['opcode'] = opcode

            return format_I(conteudos)
        case 'U':
            return 'funções U e UJ não implementadas'
        case 'UJ':
            return 'funções U e UJ não implementadas'


def main():
    print('as instruções serão em binário ou hexadecimal? (b/x)')
    r = input()
    match r:
        case 'b':
            while True:
                print('instrução (para sair, digite s): ')
                inst = f'{input()}'
                if (inst == 's'): break
                print(inst_decode(f'{inst:0>32}'))
        case 'x':
            while True:
                print('instrução (para sair, digite s): ')
                inst = f'{input()}'
                if (inst == 's'): break

                hex_to_bin = f'{bin(int(inst, 16))[2:]:0>32}'
                instrucao = inst_decode(hex_to_bin)
                print(instrucao)


if __name__ == '__main__':
    main()