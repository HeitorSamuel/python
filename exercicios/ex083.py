pilha = []

expressao = str(input('Digite uma expressão: ').strip())

for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if not pilha:
            print('Expressão inválida!')
        else:
            pilha.pop()

if '(' in pilha: 
    print('Expressão inválida!')
elif not pilha:
    print('Expressão válida!')
'''if '(' in expressao:
    print('Expressão válida')
else:
    print('Expressão inválida!')'''