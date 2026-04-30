# print("Seja bem vindo ao nosso registro de operadores!")
# nome = (input('Digite seu nome por favor:'))
# turno = (input('Digite qual seu turno:'))

# print("Bem vindo:", nome)
# print("Operador do turno:", turno)

# atividade 2
#2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
#exiba quantas peças serão produzidas em um turno de 8 horas.

# pecas = int(input('Quantas pecas foram produzidas em uma hora?'))
# total = pecas * 8
# print('Em 8 horas foram produzidas: ', total)

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar≈ 14.5 PSI) e exiba com duas casas decimais.

# pressao = int(input('Qual a pressão atual? '))
# bar = 14.5
# total = bar*pressao
# print("A pressão atual e de:", total)

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# print ("Qual o valor das ispençoes da peça?")
# nota1 = int(input(" a primeira foi em um valor de:   \n"))
# nota2 = int(input(" a segunda foi em um valor de:   \n"))
# nota3 = int(input(" a terceira foi em um valor de:   \n"))
# ntotal = ((nota1 + nota2 + nota3) /3)
# print("A nota aritimetrica foi de: "  ,ntotal)

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# temperatura = float(input("Digite a temperatura do motor (°C): "))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 > temperatura <= 70:
#     print("Normal")
# else:
#     print("ALERTA: Resfriamento Ativado!")

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# print('Bem vindo ao classificador de lotes')
# codigo = input('Digite o codigo do produto \n')
# if codigo == "A":
#     print("Alimentos")
# elif codigo == "E":
#     print('Eletronicos')
# else:
#     print("Desconhecido")

#7.  Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E obotao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.
# sensor_porta = input("Sensor da porta (aberta/fechada): ") 

# botao_emergencia = input("Botão de emergência (ligado/desligado): ") 
# if sensor_porta == "fechada" or botao_emergencia == "desligado": 
#     print("Máquina pode iniciar") 
# else: 
#     print("Máquina não pode iniciar")  

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# total = int(input("Total de peças: ")) 
# defeituosas = int(input("Peças defeituosas: ")) 
# percentual = (defeituosas / total) * 100 
# if percentual > 5: 
#  print("Revisar Processo") 
# else:
#  print("Pocesso otimizado")

#9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida ediga se está dentro da tolerância, acima ou abaixo.
# medida = float(input("Digite a medida da peça: ")) 
# if 9.8 <= medida <= 10.2: 
#     print("Dentro da tolerância") 
# elif medida < 9.8: 
#     print("Abaixo da tolerância") 
# else: 
#     print("Acima da tolerância") 

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressivade 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# for i in range(10, 0, -1): 
#     print(i) 
# print("Prensa Ativada!") 

# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.
# total = 0
# while True: 
#   peso = float(input("Digite o peso da caixa para sair: "))
#   if peso == 0: 
#        break
#   total += peso 
#   print(f"Total acumulado:", total) 

# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.Ao final, mostre qual foi a maior temperatura lida.
# maior = 0 
# for i in range(5): 
#     temp = float(input(f"Temperatura {i+1}: ")) 
#     if i == 0 or temp > maior: 
#         maior = temp
# print(f"Maior temperatura: {maior}") 

#13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.Se esgotar, exiba "Painel Bloqueado".

# senha_correta = "admin123" 
# tentativas = 3 
# while tentativas > 0: 
#     senha = input("Digite a senha: ") 
#     if senha == senha_correta: 
#         print("Acesso Permitido") 
#         break
#     else: 
#         tentativas = 1 
#         print("Acesso Negado")
# if tentativas == 0: 
#     print("Painel Bloqueado") 

