class Pessoa():
    def __init__(self, nome = 'NOME', rg = 'RG', idade = 'IDADE'):
        self.nome = nome
        self.rg = rg
        self.idade = idade
        
    def getName(self):
        return self.nome
    
    def getRG(self):
        return self.rg
    
    def getAge(self):
        return self.idade
    
    def atIdade(self, novaIdade):
        if novaIdade > 0:
            self.idade = novaIdade

class CadastroPessoas():
    def __init__(self, cadastro = {}):
        
        #self.pessoa = pessoa
        self.cadastro = cadastro
        
    def adPessoa(self, pessoa): 
        self.cadastro[pessoa.getRG()] = (pessoa.getName(), pessoa.getAge())
    
    def mostraCadastro(self):
        return self.cadastro
    
    def dadosPessoa(self, rg):
        if rg in self.cadastro.keys():
            return self.cadastro[rg]
        else:
            return {}
        
    def removerPessoa(self, rg):
        if rg in self.cadastro.keys():
            self.cadastro.pop(rg)
            return True
        else:
            return False
            
            
pessoa1 = Pessoa('Gabriel', 6145581, 22)
pessoa2 = Pessoa('Júlia', 1234567, 21)
pessoas = CadastroPessoas()

print('Cadastro inicial: ')
print(pessoas.mostraCadastro())

pessoas.adPessoa(pessoa1)
print('Primeira pessoa adcionada: ')
print(pessoas.mostraCadastro())

pessoas.adPessoa(pessoa2)
print('Segunda pessoa adcionada')
print(pessoas.mostraCadastro())
#print(pessoas.dadosPessoa(6145581))
pessoas.removerPessoa(1234568)
print(pessoas.mostraCadastro())

'''
pessoa1 = Pessoa('Gabriel', 123, 5)
print(pessoa1.getName())
print(pessoa1.getRG())
print(pessoa1.getAge())
pessoa1.atIdade(4)
print(pessoa1.getAge())
'''