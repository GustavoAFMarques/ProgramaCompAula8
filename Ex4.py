alunos = []
soma = 0
x = int(input('Digite a quantidade de aluno: '))
for i in range (x):
    nome = input(f'Digite o nome do {i+1} aluno: ').capitalize()
    nota1 = float(input(f'Digite a nota 1 {nome}: '))
    nota2 = float(input(f'Digite a nota 2 {nome}: '))
    alunos.append((nome, nota1, nota2))


for nome, nota1, nota2 in alunos:
    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f'Parabens {nome}, você foi aprovado com media {media}')
    elif media < 6:
        print(f'{nome}, sua nota esta abaixo da média com {media}')

    


