
st = ''
ctm = 0
pNome = []
ttl = []
dep = []
sal = []
uNome = []
full_data = []

# Busca e definição do arquivo
f = open("C:/Users/Public/PythonFundamentos-master/Cap04/Notebooks/arquivos/salarios.csv", 'r')
data = f.read()
rows = data.split('\n')

# Split (list in list) - Full data
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


for item in full_data:
    # Consultar list in list
    for x in range(0, len(item)):

        # Separa em listas individuais
        if ctm != 4:
            if ctm == 0:
                pNome.append(item[x])

            if ctm == 1:
                ttl.append(item[x])

            if ctm == 2:
                dep.append(item[x])

            if ctm == 3:
                sal.append(item[x])

            ctm += 1
            st += item[x] + ","
        else:
            uNome.append(item[x])
            st += item[x]
            ctm = 0

nomeC = ''
idx = 0
listNomes = []

# Formação nome completo
for idx in range(0, len(uNome)):
    nomeC = pNome[(idx + 1)][2:-1] + " " + uNome[idx][1:]
    if nomeC != '':
        listNomes.append(nomeC)

# Lista tudo
for z in range(0, len(listNomes)):
    if listNomes[z] != ' ':
        print("\nNome: " + listNomes[z])
        print("Salário: " + sal[z + 1])
        print("Título: " + ttl[z + 1])
        print("Departamento: " + dep[z + 1] + "\n")

# Faz a busca da linha especificada
"""
i = int(input("Qual o número do registro? "))  # -2  # Igual na lista

print("\nNome: " + listNomes[i])
print("Salário: " + sal[i + 1])
print("Título: " + ttl[i + 1])
print("Departamento: " + dep[i + 1] + "\n")
"""