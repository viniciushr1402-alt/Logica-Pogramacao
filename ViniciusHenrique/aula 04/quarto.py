# # # if: "Se" a condição for verdadeira
# # # elif: "Senão, se" (usado para multiplas condições)
# # # else: "Senão" (executa se nenhuma das anteriores for verdadeiras)

# # # ê e menor de idade")

# # # print("Escolha sua modalidade?")print("Expressões logicas")
# # # idade = int(input("Digite sua idade:"))

# # # if idade >= 18:
# # #     print("Você e maior de idade")
# # #     print("Pode tirar carta de motorista.")
# # # elif idade>= 16:
# # #     print("Você ainda não e maior de idade, mas já pode votar")
# # # print("Escolha sua modalidae")
# # # print("Opção 1: TI")
# # # print("Opção 2: Humanas")
# # # print("Opção 3: Exatas")
# # # modalidade = int(input("Digite sua opção de modalidade por numeros  \n"))

# # # if modalidade <= 1:
# # #    print("Você escolheu TI")
# # # elif modalidade >= 2:
# # #   print("Você escolheu Humanas")
# # # else: 
# # #    print("Você escolheu exatas")

# # # print("Categoria de Series e Filmes")
# # # print("Escolha uma categoria")
# # # print("Series = S")
# # # print("Filmes = F")
# # # categoria = input("Digite sua categoria:")
# # # if categoria == "S":
# # #      print("Sua escolha foi para Series")
# # # elif categoria == "F":
# # #   print("Sua escolha foi para Filmes")
# # # else: 
# # #     print("Você não escolheu nenhuma categoria")


# # print("Calculadora com condições")
# # print("Escolha como quer calcular")
# # print("1= Soma")
# # print("2= Subtraçâo")
# # print("3= Multiplicaçâo")
# # print("4= Divisão")
# # calculadora = float(input("Digite sua opçâo para calcular  \n"))
# # if calculadora == 1:
# #     print("1 = Você escolheu soma")
# #     soma1 = int(input("Digite o primeiro valor \n"))
# #     soma2 = int(input("Digite o segundo valor \n"))
# #     print(soma1+soma2)
# # elif calculadora == 2:
# #     print("2 = Você escolheu subtração")
# #     soma1 = int(input("Digite o primeiro valor \n"))
# #     soma2 = int(input("Digite o segundo valor \n"))
# #     print(soma1 - soma2)
# # elif calculadora == 3:
# #     print("2 = Você escolheu multiplicação")
# #     soma1 = int(input("Digite o primeiro valor \n"))
# #     soma2 = int(input("Digite o segundo valor \n"))
# #     print(soma1 * soma2)
# # elif calculadora == 4:
# #     print("2 = Você escolheu Divisão")
# #     soma1 = int(input("Digite o primeiro valor \n"))
# #     soma2 = int(input("Digite o segundo valor \n"))
# #     print(soma1 / soma2)
# # else:
# #     print("Você não escolheu nenhuma opção")




# # nota1 = int(input("Sua primeira nota foi  \n"))
# # nota2 = int(input("Sua segunda nota foi  \n"))
# # # media = (nota1 + nota2)

# # # if media >= 50:
# # #     print("Aprovado")
# # # else: 
# # #     print("Reprovado")

# # # print("Bem vindo ao semaforo")
# # # cores = int(input("qual cor deseja?  \n"))
# # # print(" 2 - Vermelho")
# # # print(" 4 - Amarelo")
# # # print (" 6 - Verde")

# # # if cores == 1:
# # #     print("Vermelho")
# # # elif cores == 2:
# # #     print("Amarelo")
# # # elif cores == 3:
# # #     print("Verde")
# # # else:

# print("Bem vindo a nossa loja!")
# print("1 = roupas 5%")
# print("2 = perfume 2%")
# print("3 = sapato  10%")

# produtos = int(input("Quais os produtos que você comprou?"))
# if produtos == 1:
#   v1 = float(input("Digite o valor do produto:  \n"))
#   qtde = int(input("Digite a qualidade do produto  \n"))
#   total = v1 * qtde * 5 / 100
#   print("A sua compra foi de: ", total)
# elif produtos == 2:
#   v1 = float(input("Digite o valor do produto:  \n"))
#   qtde = int(input("Digite a qualidade do produto  \n"))
#   total = v1 * qtde * 2 / 100
#   print("A sua compra foi de: ", total)
# elif produtos == 3:
#  v1 = float(input("Digite o valor do produto:  \n"))
# qtde = int(input("Digite a qualidade do produto  \n"))
# total = v1 * qtde * 10 / 100
# print("A sua compra foi de: ", total)



# nota1 = int(input("Sua primeira nota foi  \n"))
# nota2 = int(input("Sua segunda nota foi  \n"))
# media = (nota1 + nota2)

# if media >= 70:
#      print("Aprovado")
# elif media <= 50:
#      print("Recuperaçâo")
# else:
#    print("Reprovado")

import time
veiculos = {}

while True:
    print("1-Entrada (Ticket)")
    print("2-saida")
    print("3-sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        placa = input("Digite a placa: ")
        veiculos[placa] = time.time()
        print("Acesso registrado: Entrada liberada")

    elif opcao == "2":
        placa = input("Digite sua placa: ")

        if placa in veiculos:
            entrada = veiculos[placa]
            tempo_saida = time.time()

            tempo_total = (tempo_saida - entrada) / 3600
            valor = tempo_total * 10

            print(f"Tempo: {tempo_total:.2f} horas")
            print(f"Valor a pagar: R${valor:.2f}")
            print("Cancela liberada.")
        else:
            print("Veículo não encontrado.")

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")