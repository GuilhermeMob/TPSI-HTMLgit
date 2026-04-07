"""Guilherme Santos 
TPSI
26/03/2026"""

# Exercício 1

print("A iniciar ficha de exercícios.") # A função print é usada para exibir mensagens no console. 

# Exercício 2

nome_aluno = str
idade = int
nota_esperada = float
inscrito_exame = bool

print (nome_aluno, idade, nota_esperada, inscrito_exame) 
type(nome_aluno)
type(idade)
type(nota_esperada)
type(inscrito_exame)

# Exercício 3

nome = str (input("Insira seu primeiro nome: "))
apelido = str (input("Insira seu apelido: "))
curso = str (input("Insira seu curso: "))
idade = int(input("Insira sua idade: "))
apresentacao = nome + " " + apelido + " " + curso + " " + str(idade)
print (apresentacao)

# Exercício 4

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
total = numero1 + numero2
print ("O resultado da soma é" , str(total))