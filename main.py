# Alunos: Fabrcio Guite Pereira e João Pedro Fonseca
import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True
registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00
flag_zero = False

# memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
# memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
# memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)
    print(instrucao)
    if instrucao == 0x40:
        print('buscarEDecodificarInstrucao: instrução MOV Registrador e byte')
        return 6
    elif instrucao == 0x41:
        print('buscarEDecodificarInstrucao: instrução MOV Registrador e registrador')
        return 7
    elif instrucao == 0x00:
        print('buscarEDecodificarInstrucao: instrução ADD Registrador e byte')
        return 0
    elif instrucao == 0x01:
        print('buscarEDecodificarInstrucao: instrução ADD Registrador e registrador')
        return 1
    elif instrucao == 0x10:
        print('buscarEDecodificarInstrucao: Incrementa registrador')
        return 2
    elif instrucao == 0x20:
        print('buscarEDecodificarInstrucao: Decrementa registrador')
        return 3
    elif instrucao == 0x30:
        print('buscarEDecodificarInstrucao: instrução SOM Registrador e byte')
        return 4
    elif instrucao == 0x31:
        print('buscarEDecodificarInstrucao: instrução SOM Registrador e Registrador')
        return 5
    elif instrucao == 0x50:
        print('buscarEDecodificarInstrucao: instrução JMP byte')
        return 8
    elif instrucao == 0x60:
        print('buscarEDecodificarInstrucao: instrução CMP Registrador e Byte')
        return 9
    elif instrucao == 0x61:
        print('buscarEDecodificarInstrucao: instrução CMP Registrador e Registrador')
        return 10
    elif instrucao == 0x70:
        print('buscarEDecodificarInstrucao: instrução JZ Byte')
        return 11
    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx
    global registrador_cp
    global flag_zero

    print("implementar a lerOperadoresExecutarInstrucao")

    if idInstrucao == 0:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax += valor
        elif idRegistrador == 3:
            registrador_bx += valor
        elif idRegistrador == 4:
            registrador_cx += valor
        elif idRegistrador == 5:
            registrador_dx += valor

    elif idInstrucao == 1:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_registrador = selecionar_registrador(idRegistrador2)
        if idRegistrador == 2:
            registrador_ax += valor_registrador
        elif idRegistrador == 3:
            registrador_bx += valor_registrador
        elif idRegistrador == 4:
            registrador_cx += valor_registrador
        elif idRegistrador == 5:
            registrador_dx += valor_registrador

    elif idInstrucao == 2:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        if idRegistrador == 2:
            registrador_ax += 1
        elif idRegistrador == 3:
            registrador_bx += 1
        elif idRegistrador == 4:
            registrador_cx += 1
        elif idRegistrador == 5:
            registrador_dx += 1

    elif idInstrucao == 3:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        if idRegistrador == 2:
            registrador_ax -= 1
        elif idRegistrador == 3:
            registrador_bx -= 1
        elif idRegistrador == 4:
            registrador_cx -= 1
        elif idRegistrador == 5:
            registrador_dx -= 1

    elif idInstrucao == 4:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax -= valor
        elif idRegistrador == 3:
            registrador_bx -= valor
        elif idRegistrador == 4:
            registrador_cx -= valor
        elif idRegistrador == 5:
            registrador_dx -= valor

    elif idInstrucao == 5:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_registrador = selecionar_registrador(idRegistrador2)
        if idRegistrador == 2:
            registrador_ax -= valor_registrador
        elif idRegistrador == 3:
            registrador_bx -= valor_registrador
        elif idRegistrador == 4:
            registrador_cx -= valor_registrador
        elif idRegistrador == 5:
            registrador_dx -= valor_registrador

    elif idInstrucao == 6:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax = valor
        elif idRegistrador == 3:
            registrador_bx = valor
        elif idRegistrador == 4:
            registrador_cx = valor
        elif idRegistrador == 5:
            registrador_dx = valor

    elif idInstrucao == 7:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_registrador = selecionar_registrador(idRegistrador2)
        if idRegistrador == 2:
            registrador_ax = valor_registrador
        elif idRegistrador == 3:
            registrador_bx = valor_registrador
        elif idRegistrador == 4:
            registrador_cx = valor_registrador
        elif idRegistrador == 5:
            registrador_dx = valor_registrador

    elif idInstrucao == 8:
        valor = memoria.getValorMemoria(registrador_cp + 1)
        registrador_cp = valor - 2

    elif idInstrucao == 9:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            if registrador_ax == valor:
                flag_zero = True
        elif idRegistrador == 3:
            if registrador_bx == valor:
                flag_zero = True
        elif idRegistrador == 4:
            if registrador_cx == valor:
                flag_zero = True
        elif idRegistrador == 5:
            if registrador_dx == valor:
                flag_zero = True

    elif idInstrucao == 10:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_registrador = selecionar_registrador(idRegistrador2)
        if idRegistrador == 2:
            if registrador_ax == valor_registrador:
                flag_zero = True
        elif idRegistrador == 3:
            if registrador_bx == valor_registrador:
                flag_zero = True
        elif idRegistrador == 4:
            if registrador_cx == valor_registrador:
                flag_zero = True
        elif idRegistrador == 5:
            if registrador_dx == valor_registrador:
                flag_zero = True

    elif idInstrucao == 11:
        valor = memoria.getValorMemoria(registrador_cp + 1)
        if flag_zero == True:
            registrador_cp = valor

def calcularProximaInstrucao(idInstrucao):
    global registrador_cp
    if idInstrucao == 6:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 7:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 0:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 1:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 2:
        registrador_cp = registrador_cp + 2
    elif idInstrucao == 3:
        registrador_cp = registrador_cp + 2
    elif idInstrucao == 4:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 5:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 8:
        registrador_cp = registrador_cp + 2
    elif idInstrucao == 9:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 10:
        registrador_cp = registrador_cp + 3
    elif idInstrucao == 11:
        registrador_cp = registrador_cp + 2

def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] AX[{registrador_ax:02X}] BX[{registrador_bx:02X}] CX[{registrador_cx:02X}] DX[{registrador_dx:02X}] ZF[{flag_zero}]')

def selecionar_registrador(idRegistrador2):
    if idRegistrador2 == 2:
        return registrador_ax
    elif idRegistrador2 == 3:
        return registrador_bx
    elif idRegistrador2 == 4:
        return registrador_cx
    elif idRegistrador2 == 5:
        return registrador_dx
    else:
        return 0

if __name__ == '__main__':
    while True:
        # Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()
        # ULA
        lerOperadoresExecutarInstrucao(idInstrucao)
        dumpRegistradores()
        # Unidade de Controle
        calcularProximaInstrucao(idInstrucao)
        # apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
