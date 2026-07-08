# ==========================================
# Estruturas de Dados - Funções em Python
# ==========================================

"""
EXPLICAÇÃO DA MATÉRIA

Funções são blocos de código criados para executar uma tarefa específica.
Elas ajudam a organizar o programa, evitar repetição de código e facilitar
a manutenção.

Uma função é criada com a palavra-chave "def".

Exemplo:

def saudacao(nome):
    print(f"Olá, {nome}!")

Depois de criar a função, basta chamá-la:

saudacao("Pedro")

Também existem funções que retornam um valor usando a palavra "return".
Esse valor pode ser armazenado em uma variável ou usado em outra parte do programa.
"""

# ==========================================
# Exercício 1
# ==========================================

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

nome = input("Digite seu nome: ")
saudacao(nome)

print("\n" + "="*40)

# ==========================================
# Exercício 2
# ==========================================

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(notas):
    media = calcular_media(notas)
    status = verificar_aprovacao(media)
    print(f"Média: {media:.2f} - Situação: {status}")

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

exibir_resultado(notas)

print("\n" + "="*40)

# ==========================================
# Exercício 3
# ==========================================

def maior_menor(lista):
    return max(lista), min(lista)

numeros = []

quantidade = int(input("Quantos números deseja informar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior, menor = maior_menor(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

print("\n" + "="*40)

# ==========================================
# Desafio Extra
# ==========================================

usuarios = {
    "admin": "1234",
    "pedro": "5678"
}

def login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False

usuario = input("Usuário: ")
senha = input("Senha: ")

if login(usuario, senha):
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")# ==========================================
# Estruturas de Dados - Funções em Python
# ==========================================

"""
EXPLICAÇÃO DA MATÉRIA

Funções são blocos de código criados para executar uma tarefa específica.
Elas ajudam a organizar o programa, evitar repetição de código e facilitar
a manutenção.

Uma função é criada com a palavra-chave "def".

Exemplo:

def saudacao(nome):
    print(f"Olá, {nome}!")

Depois de criar a função, basta chamá-la:

saudacao("Pedro")

Também existem funções que retornam um valor usando a palavra "return".
Esse valor pode ser armazenado em uma variável ou usado em outra parte do programa.
"""

# ==========================================
# Exercício 1
# ==========================================

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

nome = input("Digite seu nome: ")
saudacao(nome)

print("\n" + "="*40)

# ==========================================
# Exercício 2
# ==========================================

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(notas):
    media = calcular_media(notas)
    status = verificar_aprovacao(media)
    print(f"Média: {media:.2f} - Situação: {status}")

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

exibir_resultado(notas)

print("\n" + "="*40)

# ==========================================
# Exercício 3
# ==========================================

def maior_menor(lista):
    return max(lista), min(lista)

numeros = []

quantidade = int(input("Quantos números deseja informar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior, menor = maior_menor(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

print("\n" + "="*40)

# ==========================================
# Desafio Extra
# ==========================================

usuarios = {
    "admin": "1234",
    "pedro": "5678"
}

def login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False

usuario = input("Usuário: ")
senha = input("Senha: ")

if login(usuario, senha):
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")