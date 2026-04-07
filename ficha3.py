# Exercício 1

nome = input("Insira seu nome:")
email = input("Insira seu email:")
idade = int(input("Insira sua idade:"))
preco = float(input("Insira o preço da inscrição: "))
if preco <= 0:
    pagamento = False
    print ("O preço da inscrição deve ser maior que zero.")
else:
    print("Seu nome é", nome, "e seu email é", email, "sua idade é", idade, "e o preço da inscrição é", preco)
    

# Exercício 2

artigo = input("Insira o nome do artigo:")
preco = float(input("Insira o preço do artigo: "))
quantidade = int(input("Insira a quantidade do artigo: "))
subtotal = preco*quantidade
iva = subtotal*0.23
print ("O artigo " + artigo + " que custa " + str(preco) + " e foi comprado em quantidade " + str(quantidade) + " tem um subtotal de " + str(subtotal) + " e um IVA de " + str(iva))

# Exercício 3

mes = 30
mesAno = input("Insira o mês do ano:")
consumoAgua = float(input("Insira o consumo diáriode água em litros: "))
consumoAguaMes = consumoAgua*mes
consumoMetrosCubicos = consumoAguaMes/1000
print ("O consumo mensal de água é de " + str(consumoAguaMes) + " litros, o que equivale a " + str(consumoMetrosCubicos) + " metros cúbicos.")


# Exercício 4

nomeServico = input("Insira o nome do serviço:")
horasRealizadas = float(input("Insira o número de horas realizadas: "))
valorHora = float(input("Insira o valor pago por hora: "))
pagamentoDiario = horasRealizadas*valorHora
if pagamentoDiario <= 100
valorCentena = False
else:
    valorCentena = True
    print ("O pagamento diário é de " + str(pagamentoDiario) + " e o valor é maior que 100 euros: " + str(valorCentena))
    
# Exercício 5

uniCurricular = input("Insira a unidade curricular:")
avaliacao =  input["nota1" "nota2" "nota3"]
media = avaliacao/3
if media >= 10:
alunoAprovado = True
print ("O aluno foi aprovado com média " + str(media))
else:
alunoAprovado = False
print ("O aluno foi reprovado com média " + str(media))

    
    
    
