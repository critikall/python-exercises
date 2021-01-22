# Faça um programa que tenha uma função escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(txt.center(tam))
    print('=' * tam)


# Programa principal
escreva('TITLE MAKER')
while True:
    titulo = str(input('Digite um título: ')).strip()
    escreva(titulo)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == "S" or resp == "N":
            break
        else:
            print("Erro! Por favor, digite S ou N.")
    if resp == "N":
        break
