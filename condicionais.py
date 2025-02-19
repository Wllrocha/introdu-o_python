# Estruturas Condicionais



idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor de idade")
elif idade > 60:
    print("Idoso")
else:
    print("Maior de idade")


# Classificação de números
# Escreva um programa que peça um número ao usuário e classifique-o como positivo, negativo ou zero.

numero = int(input("Digite o numero:"))

if numero > 0:
    print("Este número é POSITIVO")
elif numero < 0:
    print("Este número é NEGATIVO")
else:
    print("Este número é ZERO")


# Uso do AND 
# Escreva um programa se a média for maior ou igual a 7 e a presença for maior ou igual a 70% o aluno esta aprovado, se a media for maior ou igual a 5 e a presença maior ou igual a 50% o aluno esta de recuperção, se for menor que 5 e a presença menor que 50% o aluno esta reprovado.


media = float(input("Informe a média do aluno: "))
presenca = float(input("Informe a presença do aluno: "))

if media >=7 and presenca >= 70:
    print("Parabens voce está Aprovado!!")
elif media >= 5 and presenca >= 50:
    print("Recuperação")
else:
    print("Voce está REPROVADO!!")