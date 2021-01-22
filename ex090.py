# Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {"nome": str(input('Nome: ')), "media": float(input('Média: '))}

if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"

elif aluno["media"] < 5:
    aluno["situação"] = "Reprovado"

else:
    aluno["situação"] = "Recuperação"

print()

for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}')
