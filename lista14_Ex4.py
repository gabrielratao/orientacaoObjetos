class Urna():
    def __init__(self, local):
        self.__local = local #local da prova
       
        self.__candidatos = ['A', 'B', 'C', 'BRANCO', 'NULO']
        self.__votos = [] #aqui vai os votos de todos
        self.__contagemVotos = [] #aqui vai a contagem de votos de cada candidato/tipo(branco/nulo)
        
    def getLocal(self):
        return self.__local
    
    def votar(self, voto):  #ação de votar
        self.__votos.append(voto)
    
    def getVotacao(self):  #saber todos os votos
        return self.__votos
    
    def cntVotos(self): #contagem dos votos para cada candidato
        
        for tipoVoto in self.__candidatos:
            cnt = 0
            for voto in self.__votos:
                if voto == tipoVoto:
                    cnt += 1
            self.__contagemVotos.append(cnt)
            
    def getResultado(self): #mostra o resultado bonitinho
        resultado = [f'A: {self.__contagemVotos[0]}', f'B: {self.__contagemVotos[1]}',
                     f'C: {self.__contagemVotos[2]}', f'BRANCO: {self.__contagemVotos[3]}',
                     f'NULO: {self.__contagemVotos[4]}']
        #return self.__contagemVotos
        return resultado
    
   
    
class ZonaEleitoral():
    def __init__(self):
        self.__cadastroUrnas = []
        
        
    def adUrna(self, urna):
        self.__cadastroUrnas.append(urna)
    
    def mostraUrnas(self):
        return self.__cadastroUrnas
    
    def __str__(self):
        
        return self.__cadastroUrnas
    
urna1 = Urna('SC')

eleicao = ZonaEleitoral()
eleicao.adUrna(urna1)
print(f'mostra urnas: {eleicao.mostraUrnas}')

#urna1.votar('A')
#urna1.votar('B')
#urna1.votar('A')
#urna1.votar('BRANCO')
#print(f'Total de votos: {urna1.getVotacao()}')
#urna1.cntVotos()
#print(f'Resultado dos votos: {urna1.getResultado()}')


