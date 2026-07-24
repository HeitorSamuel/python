pilha = []
erro = False
expressao = str(input('Digite uma expressão: ').strip())

for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if not pilha:
            erro = True
            break
        else:
            pilha.pop()

if erro == True or pilha:
    print('Expressão inválida!')
else:
    print('Expressão válida!')



