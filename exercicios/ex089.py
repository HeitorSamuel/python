alunosGeral = []
aluno = []

while True:
    aluno.append(str(input('Nome: ').strip()))
    aluno.append(float(input('Nota 1: ').strip()))
    aluno.append(float(input('Nota 2: ').strip()))
    alunosGeral.append(aluno[:])
    aluno.clear()
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while perg not in 'S' and perg not in 'N':
        perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break
print(alunosGeral)