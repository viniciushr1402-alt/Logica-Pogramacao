# #1
# print("Registro de Operador")
# operador = input("Digite seu nome:")
# turno = input("Digite seu turno:")
# print(f"Operador {operador} registrando no Turno {turno}. Boa jornada!")
#  #2
# print("Cálculo de Produção")
# producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora: "))
# producao_turno = producao_hora * 8
# print(f"Quantidade de peças produzidas em um turno de 8 horas:{producao_turno}")
# #3
# print("Conversador de Unidade")
# Pressao_bar = float(input("Digite a pressão em Bar:"))
# pressao_psi = Pressao_bar * 14.5
# print(F"Pressão em PSI: {pressao_psi:.2f}")
# print(F"Pressão em PSI: {pressao_psi}",round(pressao_psi, 2))
# #4
# print("Inspeção de peças")
# nota1 = float(input("Digite a nota da inspeção 1 (0 a 10)"))
# nota2 = float(input("Digite a nota da inspeção 2 (0 a 10)"))
# nota3= float(input("Digite a nota da inspeção 3 (0 a 10)"))
# media = (nota1 + nota2 + nota3) /3
# print("Medida de qualidade da peça: ", round(media,2))
# #5
# print("Termostato Inteligente")
# temperatura = float(input("Digite a temperatura do motor em °C:"))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 <= temperatura <=70:
#     print("Normal")
# else:
#     print("ALERTA: Resfriamento Ativado!")
# #6
# print('Bem vindo ao classificador de lotes')
# codigo = input('Digite o codigo do produto \n')
# if codigo == "A":
#     print("Alimentos")
# elif codigo == "E":
#     print('Eletronicos')
# else:
#      print("Desconhecido")
# #7
# sensor_porta = input("Sensor da porta (aberta/fechada): ") 

# botao_emergencia = input("Botão de emergência (ligado/desligado): ") 
# if sensor_porta == "fechada" or botao_emergencia == "desligado": 
#      print("Máquina pode iniciar") 
# else: 
#    print("Máquina não pode iniciar")  
# #8
# total = int(input("Total de peças: ")) 
# defeituosas = int(input("Peças defeituosas: ")) 
# percentual = (defeituosas / total) * 100 
# if percentual > 5: 
#  print("Revisar Processo") 
# else:
#  print("Pocesso otimizado")
#  #9
# medida = float(input("Digite a medida da peça: ")) 
# if 9.8 <= medida <= 10.2: 
#      print("Dentro da tolerância") 
# elif medida < 9.8: 
#     print("Abaixo da tolerância") 
# else: 
#    print("Acima da tolerância")
# #10
# for i in range(10, 0, -1): 
#  print(i) 
# print("Prensa Ativada!") 
# #11
# total = 0
# while True: 
#  peso = float(input("Digite o peso da caixa para sair: "))
#  if peso == 0: 
#    break
# total += peso 
# print(f"Total acumulado:", total) 
# #12
# maior = 0 
# for i in range(5): 
#  temp = float(input(f"Temperatura {i+1}: ")) 
# if i == 0 or temp > maior: 
#  maior = temp
# print(f"Maior temperatura: {maior}") 
# #13

# senha_correta = "admin123" 
# tentativas = 3 
# while tentativas > 0: 
#      senha = input("Digite a senha: ") 
#      if senha == senha_correta: 
#          print("Acesso Permitido") 
#          break
# else: 
#          tentativas = 1 
#          print("Acesso Negado")
# if tentativas == 0: 
#      print("Painel Bloqueado") 

# estoque = 1000
# print("\nmenu")
# print("1. Adicionar itens")
# print("2. Remover itens")
# print("3. Sair")
# escolha = input("Escolha uma opçao (1, 2, 3)")

# if escolha == 1:
#    quantidade = int(input("Digite a quantidade de itens a adicionar"))
#    estoque += quantidade
#    print(F"Estoque atualizado: {estoque} itens")
# elif escolha == "2":
#    quantidade = int(input("Digite a quantidade de itens a remover"))
#    estoque -= quantidade
#    print(F"Estoque atualiazado: {estoque} itens")
#    if estoque < 10:
#       print("Estoque Critico!")
# elif escolha == "3":
#    print("Saindo do simulador de estoque")
#    break 
# else:
#  print("Opção invalida. Tente novamente") 

#15
print("Relatorio de Turno Completo")
total_pecas = 5
pecas_aprovadas = 0
for i in range(1, total_pecas + 1):
    diametro = float(input(f"Digite o diametro da peça {i} em mm"))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1
        eficiencia = (pecas_aprovadas/ total_pecas)* 100
        print(F"Total de peças aprovadas: {pecas_aprovadas}")
        print(F"Eficiencia do lote: {eficiencia:.2f}%")