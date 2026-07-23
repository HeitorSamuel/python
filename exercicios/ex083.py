pilha = []

expressao = str(input('Digite uma expressão: ').strip())

for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if '(' in pilha:
            pilha.pop()
        else:
            print('Expressão inválida!')


if not pilha:
    print('Expressão válida!')
else:
    print('Expressão inválida!')


