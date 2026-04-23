nomes = []
notas = []
x = int(input('Digite a quantidade de aluno: '))
for i in range (x):
    nome = input(f'Digite o nome do {i+1} aluno: ').capitalize()
    nota = float(input(f'Digite a nota {nome}: '))
    nomes.append(nome)
    notas.append(nota)
    
#print(nomes, notas)
while True:
    n = int(input(f'Digite o indice do aluno (0 - {x-1}): '))
    if n >= 0 and n< (x-1): break
    else: print('Digite um valor valido')
        
print(f'A nota do aluno {nomes[n]} é {notas[n]}')

nome = input('Digite o nome do aluno: ')
if nome in nomes:
    indice = nomes.index(nome)
    print(f'A nota do aluno {nomes[indice]} [e {notas[indice]}]')
else:
    print('Aluno não encontrado')
