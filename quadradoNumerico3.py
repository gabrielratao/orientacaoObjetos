#numero incial
#numero final

'''
n = 5
12345
22345
22245
22225
'''

n = int(input())
i = 1
linha = 1
numFinal = n
cnt = 0
while linha <= n:
     
    while i <= numFinal: 
    
        
        while cnt < linha:
            #print(f'linha do cnt')
            print(linha, end ='') #aqui vai alterar
            cnt += 1
            i += 1
        if i <= numFinal:
            print(i, end = '')
        i += 1
        
    cnt = 0
    print()
    i = 1
    linha += 1
    

