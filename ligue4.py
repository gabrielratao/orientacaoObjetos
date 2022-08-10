#import pygame
import random


#0 espaço disponível
#valor: 1 é a peça do jogador 1
#valor: 2 é a peça do jogador 2

matriz = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]
            ] #7x7

def tabuleiro(matriz):
    print()
    print(' INDICIES DAS COLUNAS')
    print('*0, 1, 2, 3, 4, 5, 6*')
    for coluna in matriz:
        print(coluna)
    
    return matriz

def opJogo():
    print('=+' * 20)
    print(f"{'BEM VINDO AO LGUE 4':^40}")
    print('=+' * 20)
    print()
    print('Escolha duas opções:')
    print('OPÇÃO 1: para jogar contrar o pc\nOPÇÃO 2: para jogar contra um amigo')
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
    
    
def jogada(coluna, matriz, jogador):
    tam = len(matriz)
    linha = tam - 1
    
    while matriz[linha][coluna] != 0 and linha >= 0:
        linha -= 1
        if linha == 0:
            print('COLUNA CHEIA!')
    
    matriz[linha][coluna] = jogador
    print(f'Jogada LINHA: {linha} COLUNA: {coluna}')
    tabuleiro(matriz)
    #retorna linha que foi jogada
    return linha

def verificaEmpate(matriz):
    tam = len(matriz)
    linha = 0
    cntZeros = 0
    while linha < tam:
        coluna = 0
        while coluna < tam:
            if matriz[linha][coluna] == 0:
                cntZeros += 1
            coluna += 1
        linha += 1
    if cntZeros == 0:
        return True
    else:
        return False
    
def entradaValidaJogador():
    entrada = int(input('Escolha sua coluna: '))
    while entrada < 0 or entrada > 6:
        print('Entrada inválida, escolha valores entre 0 e 6')
        entrada = int(input('Escolha sua coluna: '))
    return entrada

def entradaPC():
    entrada = random.randint(0, 6)
    print(f'entrada escolhida do pc {entrada}')
    return entrada
    


def obtemElementosVertical(matriz, linha, coluna):
    #ELEMENTOS VERTICAL:
    
    tam = len(matriz)
    
    limiteBaixo = linha + 3
    limiteCima = linha - 3
    
    if limiteBaixo > (tam - 1):
        limiteBaixo = (tam - 1)
    if limiteCima < 0:
        limiteCima = 0
        
    linhaAtual = limiteBaixo
    elementos = []
    while linhaAtual >= limiteCima:
        elementos.append(matriz[linhaAtual][coluna])
        linhaAtual -= 1
    return elementos
    
    
    
def verificaVertical(elementos):
    cnt1 = 0
    cnt2 = 0
    
    for elemento in elementos:
        
        if elemento == 1:
            cnt1 += 1
        elif cnt1 == 4:
            break
        else:
            cnt1 = 0
    for elemento in elementos:
        if elemento == 2:
            cnt2 += 1
        elif cnt2 == 4:
            break
        else:
            cnt2 = 0
        
    if (cnt1 == 4) or (cnt2 == 4):
        return True
    else:
        return False

def obtemElementosLados(matriz, linha, coluna):
    tam = len(matriz)
    #linha = obterLinha(matriz, coluna, jogador)
    
    limiteDireita = coluna + 3
    limiteEsquerda = coluna - 3
    #                      (6)
    if limiteDireita > (tam - 1):
        limiteDireita = (tam - 1)
    if limiteEsquerda < 0: #
        limiteEsquerda = 0
    
    colunaAtual = limiteEsquerda
    elementos = []
    while colunaAtual <= limiteDireita:
        elementos.append(matriz[linha][colunaAtual])
        colunaAtual += 1
        
    return elementos

def verificaLados(elementos):
    cnt1 = 0
    cnt2 = 0
  
  
    for elemento in elementos:
        if elemento == 1:
            cnt1 += 1
        elif cnt1 == 4:
            break
        else:
            cnt1 = 0
    for elemento in elementos:
        if elemento == 2:
            cnt2 += 1
        elif cnt2 == 4:
            break
        else:
            cnt2 = 0
            
        
            
    if (cnt1 == 4) or (cnt2 == 4):
        return True
    else:
        return False
    

def verificaVitoria(matriz, linha, coluna, jogador):
    #VERIFICAÇÃO LADOS
    elementosLaterais = obtemElementosLados(matriz, linha, coluna)
    
    #VERIFICAÇÃO CIMA
    elementosVerticais = obtemElementosVertical(matriz, linha, coluna)
    
    if verificaVertical(elementosVerticais):
        return True
    
    elif verificaLados(elementosLaterais):
        return True
    
    else:
        return False
   
    
    
    
    

def jogo():
    
    #escolher opção de jogo
    
    opJogo_Escolhida = opJogo()
    while opJogo_Escolhida == False:
        opJogo_Escolhida = opJogo()
    nJogadas = 1
    tabuleiro(matriz)
    vitoria = False
    empate = False
    while vitoria != True and empate != True:
        
        
        print()
        #verifica qual é o jogador:
        jogador = vezJogador(nJogadas)
        print(f'Vez do jogador {jogador}')
        
        #a partir da opJogo obtem a entrada da coluna  1 contra pc e 2 contra outro jogador
        if opJogo_Escolhida == 1:
            #VEZ DO PC que ja retorna uma coluna válida
            entrada = entradaPC()
            empate = verificaEmpate(matriz)
            if empate == False:
                linha = jogada(entrada, matriz, jogador)
            
            #analise se há vitoria
            vitoria = verificaVitoria(matriz, linha, entrada, jogador) 
            nJogadas += 1
            
            #passa para o jogador jogar
            jogador = vezJogador(nJogadas)
            print(f'Vez do jogador {jogador}')
            entrada = entradaValidaJogador()
            empate = verificaEmpate(matriz)
            if empate == False:
                linha = jogada(entrada, matriz, jogador)
            
            #analise se há vitoria
            vitoria = verificaVitoria(matriz, linha, entrada, jogador) 
            nJogadas += 1
            
            
        elif opJogo_Escolhida == 2:
            entrada = entradaValidaJogador()
            empate = verificaEmpate(matriz)
            if empate == False:
                linha = jogada(entrada, matriz, jogador)
            
            #analise se há vitoria
            vitoria = verificaVitoria(matriz, linha, entrada, jogador) 
            nJogadas += 1
        
    if vitoria == True:
        print()
        print('=+' * 20)
        print(f"{'TEMOS UM GANHADOR':^40}")
        print('=+' * 20)
        print()
        print(f'Parabéns jogador {jogador} você ganhou o LIGUE 4!')
        
    elif empate == True:
        print()
        print('=+' * 20)
        print(f"{'TEMOS UM EMPATE':^40}")
        print('=+' * 20)
        print()
        print('Não há mais espaços disponíveis!')
        
    
        
    
    
#ativa função do jogo  
jogo()
        
        
        
    
    
    
    
    
    
    
    
    
    
