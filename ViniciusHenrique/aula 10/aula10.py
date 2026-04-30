

# Projeto cancela automatica
# criar um algoritimo que consiga gerenciar entrada e saida de veiculos, inserindo valores por hora permanecida.
# A froma de entrada e saida deve ser especificada e permitir o usuario inserir os dados nescessarios para registro do veiculo.

# 1 - Pressionar botão , imprimiu um ticket
# Calcular tempo de permanencia
# Pagar o ticket
# Devolver o ticket na saída
#Liberar e fechar cancelas

# 2 - Acesso por TAGs (Sem parar, Connect Car...)
# Calcular tempo de permanencia
# Gerar pagamento em fatura
# Liberar e fechar cancelas

# 3 - Erros
# Verificar sinal de trsnamissão da TAG
# Verificar acessso por ticket ou TAG ao mesmo tempo
# Perdeu ticket (levantar informações)
# Problemas com cancela

import time

print("Bem Vindo ao nosso estacionamento!")
veiculos = {}

while True:
    print("\n1-Entrada (Ticket)")
    print("2-Saída")
    print("3-Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        placa = input("Digite a placa: ")
        veiculos[placa] = {
            "entrada": time.time(),
            "ativo": True
        }
        print("Acesso registrado: Entrada liberada")

    elif opcao == "2":
        placa = input("Digite sua placa: ")

        if placa in veiculos and veiculos[placa]["ativo"]:
            entrada = veiculos[placa]["entrada"]
            tempo_saida = time.time()

            segundos = tempo_saida - entrada
            minutos = segundos / 60
            horas = segundos / 3600

            valor = horas * 10 

            print(f"Tempo: {minutos:.1f} minutos ({horas:.2f} horas)")
            print(f"Valor a pagar: R${valor:.2f}")
            print("Cancela liberada")

            veiculos[placa]["ativo"] = False 

        elif placa in veiculos:
            print("Veículo já saiu!")

        else:
            print("Veículo não encontrado!")

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")