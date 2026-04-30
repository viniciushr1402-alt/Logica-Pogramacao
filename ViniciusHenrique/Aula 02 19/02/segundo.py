# # funções

# a = 1 #a é uma variavel
# b = 2 
# c = a + b 
# print ('O valor de A e B é: ', c)
 
#  # Variáveis são formas de armazenar informações

# # Função Input
# # Ir permitir inserir informações
# input("Qual é seu nome?")

# # Operadores Matemáticos 
# # + = soma
# # - = subtração
# # * = multiplicação
# # / = divisão
# # Toda vez que quiser que o programa jogue alguma informação para a o proxima linha eu tenho que usar o \n para quebrar a linha dentro de a

# #  Exemplo 1 
# v1 = input("Digite o primeiro valor: \n")
# v2 = input("Digite o segundo valor: \n")
# vtotal = v1 + v2
# print("Qual o resultado?" , vtotal)

# # int = retorna valores initeiros Ex: 1, 5
# # float = valores com casas decimais Ex: 10.2 , -10.1

# # Exemplo 2 
# x1 = int(input("Digite o primeiro valor: \n"))
# x2 = int(input("Digite o segundo valor: \n"))
# xtotal = x1 - x2
# print("Qual é o valor do X \n" , xtotal)

# # Exemplo 3 
# print('Vamos Calcular?')
# print('iniciamos a multiplicação')
# x1 = int(input("Digite o primeiro valor: \n"))
# x2 = int(input("Digite o segundo valor: \n"))
# xtotal = x1 * x2
# print("Qual o valor do X \n " , xtotal)

# # Exemplo 4 
# print('Vamos Calcular?')
# print('iniciamos a divisão')
# x1 = int(input('Digite o primeiro valor: \n'))
# x2 = int(input('digite o segundo valor \n'))
# xtotal = x1 / x2
# print("Qual o valor do X \n " , xtotal)

# print('Vamos dividir \n')
# d1 = float(input('Digite o primeiro valor desejado \n'))
# d2 = float(input('Digite o segundo valor deejado \n'))
# dtotal = d1 / d2
# print('Sua divisão é: \n' , dtotal)

# #Concatenar
# print('Eu gosto de programar \n' + ' \n Python \n')

# EXERCICIO

# input('Digite seu nome? \n')
# input('Qual seu curso? \n')
# input('Qual o sua idade? \n')
# input('Qual seu hobby \n')

# nome = input('Digite seu nome? \n')

# # idade = input('Digite sua idade? \n')
# # hobbie = input ('Digite seu hobbie? \n')

# # print('As informações são: \n' , 'Seu nome é \n' , nome +  '\n Sua idade é? \n ' , idade + ' \n Seu curso é? \n' , curso + ' \n Seu hobbie é? \n ' , hobbie)

# # print("Bem vindo a nossa calculadora de IMC")
# # peso = float(input("Digite seu peso:  "))
# # altura = float(input("Digite seu altura:   "))
# # total = peso / (altura * altura)
# # print("Qual é o valor do X \n" , total)

# # x1 = float(input("Digite o primeiro valor desejado\n"))
# # x2 = float(input("digite o segundo valor desejado \n"))
# # print('A soma é \n' , x1 + x2)
# # print('A subtração é \n' , x1 - x2)
# # print('A divisão é \n' , x1 / x2)
# # print('A multiplicação é \n' , x1 *
  
# produto = input("Que produto vocé comprou?   \n")
# quantidade = float(input("Qual a quantidade?   \n"))
# valor = float(input("digite o valor   \n"))
# print("O valor da sua compra foi:" , (quantidade * valor))
# print("E a quantidade compradada foi" , quantidade)


# try:
#     n = int(input("Quantos números? "))
#     soma = 0

#     for _ in range(n):
#         soma += int(input("Número: "))

#     print("Média:", soma / n)

# except ValueError:
#     print("Erro: digite apenas números inteiros.")

import time

veiculos = {}

while True:
    print("\n1 - Entrada (ticket)")
    print("2 - Saída")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        placa = input("Digite a placa: ").upper()
        veiculos[placa] = time.time()
        print("Ticket gerado. Entrada registrada.")

    elif opcao == "2":
        placa = input("Digite a placa: ").upper()

        if placa in veiculos:
            tempo_entrada = veiculos[placa]
            tempo_saida = time.time()

            tempo_total = (tempo_saida - tempo_entrada) / 3600
            valor = tempo_total * 10 

            print(f"Tempo: {tempo_total:.2f} horas")
            print(f"Valor a pagar: R${valor:.2f}")

            del veiculos[placa]
            print("Cancela liberada.")
        else:
            print("Veículo não encontrado.")

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")
