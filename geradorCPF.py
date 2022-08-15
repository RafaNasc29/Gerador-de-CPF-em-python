"""
    Gerador de CPF
"""

from random import randint
num = str(randint(100000000, 999999999))

novoCPF = num
Nprim = ''
contP = 10
contS = 11
somaP = 0
somaS = 0
primeiro = 0
segundo = 0

# Para o Primeiro Digito
for n in num[0:9]:
    if not n == '.':            # Retira os "." e "-" do cpf digitado
        Nprim += n

for x in Nprim:
    if x.isnumeric():           # Verifica se foram realmente digitados números
        x = int(x)

    multP = x * contP
    somaP = somaP + multP
    contP -= 1

# Realiza os cálculos para obter os últimos 2 dígitos do CPF
resultadoP = 11 - (somaP % 11)

if resultadoP > 9:
    primeiro = 0
else:
    primeiro = resultadoP

Nprim += str(primeiro)

# Para o Segundo Digito
for n in Nprim:
    if n.isnumeric():
        n = int(n)

    multS = n * contS
    somaS = somaS + multS
    contS -= 1

resultadoS = 11 - (somaS % 11)

if resultadoS > 9:
    segundo = 0
else:
    segundo = resultadoS

# Passa o resultado para novoCPF e mostra na tela o cpf obtido
Nprim += str(segundo)

novoCPF += Nprim[9:11]

# print(novoCPF)
print(f'{novoCPF[0:3]}.{novoCPF[3:6]}.{novoCPF[6:9]}-{novoCPF[9:11]}')
