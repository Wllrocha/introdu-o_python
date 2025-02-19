# Conversão de Tipos

"""
Obs: Não se pode colocar inteiro e str juntos
        Exemplo:
        idade1 = "2"
        idade2 = 1
        print(idade1 + idade2)
"""
idade = '26'

print(idade, type(idade))

# Convertendo a Variavel
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# Informando altura
altura = float(input("Informe sua altura: "))

print(altura, type(altura))