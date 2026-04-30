# # 1. O laço "for" (Repetições Determinadas)
# # Use o "for" quando você sabe exatamente quantas vezes algo deve acontecer(como ler 10 sensores ou processar uma lista de peças)
# # Exemplo: relatorio de produção diaria
# # imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# # # Exemplo 1 
# # # for lote in range(1, 6):
# # #     print(f"Processando lote numero {lote}...")
# # #     print("Qualidade verificada. [OK]")
# # #     print("Produção do dia finalizada!")

# # # for carros in range(10):
# # #     print(f"Quantidade de carros {carros}")

# # # #exemplo 2 
# # # # contar ate 4 
# # # for a in range(5):
# # #     print(a)


# # # # exemplo 3 
# # # # pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso"]
# # # # maquinas = ["Maquina 1", "Maquina 2",]

# # # # for item in pecas:
# # # #     print(f"Item em estoque: {item}")
# # # #     for maq in maquinas:
# # # #         print(f"Maquinas que temos {maq}")

# # # # Exercicio 1 
# # # # 1. Contador de produção 
# # # # uma esteira processa 10 peças por ciclo.Crie um programa que use um for para contar de 1 a 10 e, para cada numero, imprima: "Peça n X processada com sucesso". no final exiba "ciclo de produção concluido"


# # # # for i in range(1, 11):
# # # #     print("Peça nº", i, "processada com sucesso")
# # # # print("Ciclo de produção concluído")

# # # # imagine a produçãode frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi com uma quantidade de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi.


# # # # frutas = ["Banana", "Manga", "Melancia", "Abacaxi"]
# # # # quantidades = [10, 5, 10, 13]

# # # # total = 0

# # # # for i in range(len(frutas)):
# # # #     print(frutas[i], "-", quantidades[i])
# # # #     total += quantidades[i]

# # # # print("Total de frutas:", total)

# # # # # Montar a tabuada do 5 inicialmente pode ser usado por um valor fixo e depois usar a pergunta
# # # numero=int(input("Você deseja qual numero da tabuada?"))

# # # for i in range(1, 11):
# # #    print(numero, "x" , i, "=", numero * i)

# # # #    # USE O WHILE QUANDO VOCE NAO SABE QUANDO VAI PARAR. ELE DEPENDE DE UMA CONDIÇÃO (COMO UM SENSOR DE SEGURANÇA OU UM BOTÃO DE EMERGENCIA)
# # #    # EXEMPLO: MONITOR DA TEMPERATURA (LOOP INFINITO CONTROLADO)

# # # # temperatura = 25
# # # # while temperatura < 40:
# # # #        print(f"Temperatura atual: {temperatura}°C. Sistema operando...")  
# # # #        temperatura += 3 #Simulando o aquecimento da maquina 
# # # # print("ALERTA! Temperatura atingiu o limite. Desligado montor...")

# # # # opcao = ""

# # # # while opcao != "sair":
# # # #     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
# # # #     if opcao != "sair":
# # # #         print(f"Dado '{opcao}' registrado no banco de dados.")
# # # # print("Sistema encerrado")

# # # print("MENU DE SERIES")
# # # print("Opção 1 - Stranger Things")
# # # print("Opçao 2 - Dark")
# # # print("Opção 3 - Bem-Vindos a Derry")
# # # print("Opção 4 - Prison Break")

# # # opcao= int(input("Escolha uma opção: "))


# # # if opcao == 1:print("Você escolheu Stranger Things")
# # # elif opcao == 3:print("Você escolheu Dark")
# # # elif opcao == 3:print("Você escolheu Bem-Vindo a Derry")
# # # elif opcao == 4:print("Você escolheu Prison Break")
# # # else:print("Saindo do Menu")
# # # leituras = [70,75,82,98,110,85,80]
# # # for temp in leituras:
# # #    if temp > 100:
# # #       print(f"CRITICO: {temp}ºC detectado! Acionando parada de emergencia.")
# # #       break #O loop para aqui não lê os proximos valores(85 e 80)
# # # print(F"Temperatura esta em {temp}°C. Operação normal.")

# # # print("Sistema desligado. Aguardando manurenção")

# # # materias = ["metal", "metal", "plastico", "metal", "vidro", "metal"]

# # # peca = ""

# # # materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# # # for peca in materiais:
# # #     if peca !="metal":
# # #         print(F"Aviso: a peça de {peca} detectada. Desviando para descarte...")
# # #         continue #Pula o restante do codigo abaixo e vai para a proxima peça
    
# # #     #Este codigo só roda se a peça for de metal
# # #     print(F"Processando peça de {peca}. furando e polindo...")

# # #     print("Fim do lote de produção")

# #    # tente criar um codigo que conte de 1 a 10, mas use o continue para nao imprimir o numero 5 (simulando uma falha de sensor especifica no item 5).

# # for i in range(1, 11):
# #     if i == 5:
# #         continue
# #     print(i)
    
# #     from time import sleep 
# #     for i in range (1,11)
# #     if i == 5:
# #         print(F"Falha ao ler o n° {i}")
# #         sleep(1.8)
# #         continue
# #     print(i)
# #     sleep(0.7)
# #     print("Acabou")

# #     # Simule um semafaro com parada para cada cor, Determine um tenpo que decaia para que quando mudar para tal cor ele represente uma pausa, com tempo e ainda com opçoes


# import time

# print(" SEMÁFORO ")

# verde = 10
# amarelo = 9
# vermelho = 8

# print("VERDE")
# time.sleep(verde)
# print("AMARELO")
# time.sleep(amarelo)
# print("VERMELHO")
# time.sleep(vermelho)
# print("Ciclo finalizado!")

# exercicio 4 - Soma de cargas de energia(for)
# Uma fabrica tem 5 maquinas. Peça ao usuario(vai input dentro do loop) o consumo em KWh de cada uma das maquinas. Ao final do loop, o programa deve exibir o consumo total da fabrica.

# exercicio 5  identificador de peças defeituosas ( for + if
# percorra uma lista de medidas de pecas:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# o padrao de qualidade aceita apenas pecas com exatamente 50.0 ou mais.
#Use um for para ler a lista e, para cada peça, diga se ela esta "Aprovada" ou "rejeitada"

# total = 0
# for i in range (1, 6):
#     consumo = float(input(f"Digite o consumo da maquina {i} (kWh) :"))
#     total += consumo

#     print(f"O consumo total da fabrica: {total} (kwh) ")



# print("Identifação de peças: ")
# medidas =  [50.1, 49.8, 52.0, 50.0, 48.5]
# # total = float(input("Digite o valor"))
# for med in medidas:
    
#     if med > 50.0:
#        print(f"{medidas} = Aprovada")
# else:
#     print(f"{medidas} = Reprovada")

# exercicio: uma balança industrial esta pesando um lote 6, sacos de insumos. o peso ideal de cada saco e 50kg, mas o sistema aceita variaçoes.

pesos = [50.2, 49.5, 51.0, 48.9, 50.0, 52.3]
for peso in pesos:
    if 48 <= peso <= 52:
        print(peso, "- Dentro do padrão")
    else:
        print(peso, "- Fora do padrão")

#criei um programa que recebe dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da maquina seguindo esta hierarquia: 
# Critico (Prioridade 1) se a pressão for maior que 100 ou as horas de uso forem maiores que 10.000.
# mensagem: "PARADA IMEDIATA: Risco de falha catastofrica.
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive)

