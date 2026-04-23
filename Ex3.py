nomes = []

x = int(input('Digite a quantidade de aluno: '))

for i in range(x):
    nome = input(f'Digite o nome do {i+1}º aluno: ').capitalize()
    nomes.append(nome)

for i, nome in enumerate(nomes, start=1):
    print(f'[{i}] - {nome}') 