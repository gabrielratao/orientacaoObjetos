#import pygame
import random

'''
função para ver qual a utlima posição jogada na coluna
e adicionar a nova jogada. Tudo na mesma função
'''

#0 espaço disponível
#1 peça jogador 1
#2 peça jogador 2
matriz = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]
            ] #7x7

def tabuleiro(matriz):
    for coluna in matriz:
        print(coluna)
    return matriz

def opJogo():
    
    print('Bem vindo ao jogo')
    print('Escolha opção 1 para jogar contrar o pc \nou 2 para jogar contra um amigo')
    op = int(input('Opção escolhida: '))
    
    if op == 1:
        return 1
    elif op == 2:
        return 2
    else:
        return False
    
def vezJogador(nJogadas):
    if nJogadas % 2 == 1:
        return 1
    else:
        return 2
    
    
def colunaValida(coluna, matriz, jogador):
    
    
    tam = len(matriz)
    linha = tam - 1
    
    while linha >= 0:
        #matriz[linha][coluna] = matriz[linha][coluna] + 1
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = jogador
            linha = 0
        '''if (matriz[linha][coluna] == 1) or (matriz[linha][coluna] == 2):
            if linha == 0:
                print('entrada valida')
                return True
        else:
            matriz[linha][coluna] = jogador'''
            
        linha -= 1
        
    
    tabuleiro(matriz)
        
            

    
def entradaValida(opJogo_Escolhida):
    if opJogo_Escolhida == 2:
        entrada = int(input('Escolha sua coluna: '))
        while entrada < 0 or entrada > 6:
            print('Entrada inválida, escolha valores entre 0 e 6')
            entrada = int(input('Escolha sua coluna: '))
    elif opJogo_Escolhida == 1:
        entrada = random.randint(0, 6)
        print(f'entrada escolhida do pc {entrada}')
    return entrada

    
    
#def vitoria():
    
    
    

def jogo():
    
    #escolher opção de jogo
    opJogo_Escolhida = opJogo()
    nJogadas = 1
    tabuleiro(matriz)
    while True:
        
        
        
        
        print()
        #verifica qual é o jogador:
        jogador = vezJogador(nJogadas)
        print(f'Vez do jogador {jogador}')
        #pega entrada válida da coluna
        entrada = entradaValida(opJogo_Escolhida)

        #verifica se essa coluna á válida        
        colunaValida(entrada, matriz, jogador)
        nJogadas += 1
    
    
        
    
    
    
jogo()
        
        
        
    
    
    
    
    
    
    
    
    
    