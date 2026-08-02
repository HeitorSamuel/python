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
print('-='*30)
print(f'{'N°':<4}{'NOME':<12}{'MÉDIA'}')
print('-'*30)
for pos, al in enumerate(alunosGeral):
    media = (al[1] + al[2]) / 2
    print(f'{pos:<4}{al[0]:<12}{media:.1f}')
while True:
    print('-'*30)
    mostrNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): ').strip())
    if mostrNotas == 999:
        break
    else:
        if mostrNotas == pos:
            print(f'Notas de {al[0]} são {al[1]}')