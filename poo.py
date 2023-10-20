class ContaBancaria():
    #CONSTRUTOR
    def __init__(self, nome, cpf, email, telefone, numConta):

        #ATRIBUTOS
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.numConta = numConta
        self.saldo = 0

    #MÉTODOS
    def getName(self):
        return self.nome
    
    def getCPF(self):
        return self.cpf

    def getEmail(self):
        return self.email
    
    def getTelefone(self):
        return self.telefone
    
    def getNumConta(self):
        return self.numConta
    
    def getSaldo(self):
        return self.saldo

    def setName(self, nome):
        self.nome = nome
    
    def setEmail(self, email):
        self.email = email

    def depositar(self, valor):
        self.saldo = self.saldo + valor
    
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
            return False
        else:
            self.saldo = self.saldo - valor
            print(f'Saque realizado com sucesso\nNovo saldo: {self.saldo}')
            return True
        
    def transferir(self, valor, conta):
        if valor < self.saldo:
            conta.depositar(valor)
            print('Transferência realizada com sucesso')
            return True
        else:
            print('Saldo insuficiente')
            return False
        
    def __str__(self):
        return f'Conta de {self.nome} numero {self.numConta}'


conta1 = ContaBancaria(nome='Gabriel', cpf=123, email='gabi@gmail', telefone=456, numConta=0)
conta2 = ContaBancaria(nome='José', cpf=456, email='jose@gmail', telefone=789, numConta=1)
# print(conta1.saldo)
# conta1.getName()

print(conta1)
# conta1.setEmail('joao@joao')
# print(conta1.getEmail())


# print(conta1.getSaldo())
# conta1.depositar(300)
# print(conta1.getSaldo())
# print('saldos conta 2')
# print(conta2.getSaldo())
# conta1.transferir(200, conta2)
# print(conta1.getSaldo())