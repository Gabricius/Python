
colunas = []
maxColunas = 0

# listArquivo = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
listArquivo = [['1'], ['1', '2', '3','4'], ['1', '2', '3','4'],['1','2','3','4','5']]

# Criando o máximo de colunas da matriz
for lista in listArquivo:
    for item in lista:
        if lista.index(item)+1 >= maxColunas:
            colunas += [[]]
            maxColunas = len(lista)

# Retirando uma lista vazia no final
colunas.pop(len(colunas)-1)

# Organizando cada item com a sua coluna
for linhas in listArquivo:
    for count in range(0, len(linhas)):
        colunas[count].append(linhas[count])

print(colunas)
