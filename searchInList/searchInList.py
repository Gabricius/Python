nomeCompleto = ''
listTitulos = []
listDepartamentos = []
listSalarios = []
listPrimeiroNome = []
listUltimoNome = []
listNomeCompleto = []
full_data = []

# Busca e definição do arquivo
with open("searchInList/salarios.csv", 'r') as f:
    data = f.read()
rows = data.split('\n')

# Split (list in list) - Full data
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

for item in full_data:
    coluna = 0
    # Consultar list in list
    for x in range(0, len(item)):

        # Separa os items por coluna
        if coluna == 0:
            listPrimeiroNome.append(item[x])

        if coluna == 1:
            listTitulos.append(item[x])

        if coluna == 2:
            listDepartamentos.append(item[x])

        if coluna == 3:
            listSalarios.append(item[x])

        if coluna == 4:
            listUltimoNome.append(item[x])

        coluna += 1

# Formação nome completo
for idx in range(0, len(listUltimoNome)):
    nomeCompleto = listPrimeiroNome[(idx + 1)][2:-1] + " " + listUltimoNome[idx][1:]
    if nomeCompleto != '':
        listNomeCompleto.append(nomeCompleto)

# Lista tudo
for counter in range(0, len(listNomeCompleto)):
    if listNomeCompleto[counter] != ' ':
        print("\nNome: " + listNomeCompleto[counter])
        print("Salário: " + listSalarios[counter + 1])
        print("Título: " + listTitulos[counter + 1])
        print("Departamento: " + listDepartamentos[counter + 1] + "\n")

# Faz a busca da linha especificada
"""
indexItem = int(input("Qual o número do registro? "))  # -2  # Igual na lista

print("\nNome: " + listNomeCompleto[indexItem])
print("Salário: " + listSalarios[indexItem + 1])
print("Título: " + listTitulos[indexItem + 1])
print("Departamento: " + listDepartamentos[indexItem + 1] + "\n")
"""
