conjPalavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in conjPalavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    