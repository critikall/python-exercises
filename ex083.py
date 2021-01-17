# Crie um programa onde o usuário digite uma expressão(matemática) qualquer que
# use parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: ')).strip()

parenteses = []

for i in exp:
    if i == '(':
        parenteses.append('(')
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
