# Sistema de Cancelas Automáticas
# Gerencia entrada e saída de veículos com Ticket ou TAG
# Calcula tempo de permanência e valor a pagar

import time
from datetime import datetime

# ============================================
# DADOS DO SISTEMA
# ============================================

# Veículos por Ticket (armazena: placa -> horaEntrada)
veiculos_ticket = {}

# Veículos por TAG (armazena: tag -> dados do veículo)
# Estrutura: {'TAG123': {'placa': 'ABC-1234', 'hora_entrada': timestamp}}
veiculos_tag = {}

# Histórico de operações (para consultas)
historico = []

# Valor por hora (em reais)
VALOR_POR_HORA = 10.0
VALOR_MINIMO = 10.0  # Vale como taxa mínima para ticket perdido

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def mostrar_menu():
    """Mostra omenu principal"""
    print("\n" + "="*40)
    print("     SISTEMA DE CANCELA AUTOMÁTICA")
    print("="*40)
    print("1 - ENTRADA (Ticket)")
    print("2 - SAÍDA (Ticket)")
    print("3 - ENTRADA (TAG)")
    print("4 - SAÍDA (TAG)")
    print("5 - ERROS E PROBLEMAS")
    print("6 - CONSULTAR HISTÓRICO")
    print("0 - SAIR")
    print("="*40)

def registrar_historico(tipo, placa, entrada, saida, valor):
    """Registra operação no histórico"""
    dados = {
        'tipo': tipo,
        'placa': placa,
        'entrada': entrada,
        'saida': saida,
        'valor': valor
    }
    historico.append(dados)

def calcular_valor(hora_entrada, hora_saida):
    """Calcula valor berdasarkan tempo de permanência"""
    tempo = (hora_saida - hora_entrada) / 3600  # Converte para horas
    
    # Arredonda para cima se passar de 15 minutos
    if tempo - int(tempo) > 0.25:
        tempo = int(tempo) + 1
    else:
        tempo = int(tempo)
    
    # Mínimo de 1 hora
    if tempo < 1:
        tempo = 1
    
    valor = tempo * VALOR_POR_HORA
    return tempo, valor

def formatar_hora(timestamp):
    """Formata timestamp para hora legível"""
    return datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")

# ============================================
# 1 - ENTRADA POR TICKET
# ============================================

def entrada_ticket():
    """Registra entrada de veículo por ticket"""
    print("\n--- ENTRADA POR TICKET ---")
    
    placa = input("Digite a placa do veículo: ").upper().strip()
    
    if not placa:
        print("ERRO: Placa inválida!")
        return
    
    # Verifica se veículo já está dentro
    if placa in veiculos_ticket:
        print(f"ERRO: Veículo {placa} já está dentro!")
        print(f"Entrada registrada às: {formatar_hora(veiculos_ticket[placa])}")
        return
    
    # Registra entrada
    hora_entrada = time.time()
    veiculos_ticket[placa] = hora_entrada
    
    # Gera número do ticket (número aleatório)
    numero_ticket = int(hora_entrada % 10000)
    
    print("\n*** TICKET GERADO ***")
    print(f"Número do Ticket: {numero_ticket}")
    print(f"Placa: {placa}")
    print(f"Entrada: {formatar_hora(hora_entrada)}")
    print("=====================")
    
    registrar_historico("ENTRADA-TICKET", placa, hora_entrada, None, 0)
    print("Entrada liberada! Bom trânsito!")

# ============================================
# 2 - SAÍDA POR TICKET
# ============================================

def saida_ticket():
    """Registra saída de veículo por ticket"""
    print("\n--- SAÍDA POR TICKET ---")
    
    placa = input("Digite a placa do veículo: ").upper().strip()
    
    if not placa:
        print("ERRO: Placa inválida!")
        return
    
    # Verifica se veículo está dentro
    if placa not in veiculos_ticket:
        print(f"ERRO: Veículo {placa} não encontrou-se dentro!")
        print("Verifique se a placa está correta.")
        return
    
    hora_entrada = veiculos_ticket[placa]
    hora_saida = time.time()
    
    # Calcula tempo e valor
    tempo, valor = calcular_valor(hora_entrada, hora_saida)
    
    print("\n*** CUPOM FISCAL ***")
    print(f"Placa: {placa}")
    print(f"Entrada: {formatar_hora(hora_entrada)}")
    print(f"Saída: {formatar_hora(hora_saida)}")
    print(f"Tempo: {tempo} hora(s)")
    print(f"Valor: R$ {valor:.2f}")
    print("=====================")
    
    # Confirma pagamento
    print("\nFavor dirigir até o caixa para pagamento.")
    pagamento = input("Pagamento realizado? (S/N): ").upper()
    
    if pagamento == "S":
        # Remove veículo
        del veiculos_ticket[placa]
        print("\n*** CANCELA LIBERADA ***")
        print("Obrigado! Volte sempre!")
        registrar_historico("SAIDA-TICKET", placa, hora_entrada, hora_saida, valor)
    else:
        print("Pagamento não realizado. Saída bloqueada!")

# ============================================
# 3 - ENTRADA POR TAG
# ============================================

def entrada_tag():
    """Registra entrada de veículo por TAG"""
    print("\n--- ENTRADA POR TAG ---")
    
    # Menu de opções
    print("1 - Registrar nova TAG")
    print("2 - Usar TAG existente")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        # Registrar nova TAG
        tag = input("Digite o número da TAG: ").upper().strip()
        placa = input("Digite a placa do veículo: ").upper().strip()
        
        if not tag or not placa:
            print("ERRO: TAG ou Placa inválidos!")
            return
        
        # Verifica se TAG já existe
        if tag in veiculos_tag:
            print(f"ERRO: TAG {tag} já está cadastrada!")
            return
        
        # Registra TAG
        hora_entrada = time.time()
        veiculos_tag[tag] = {
            'placa': placa,
            'hora_entrada': hora_entrada
        }
        
        print("\n*** TAG CADASTRADA ***")
        print(f"TAG: {tag}")
        print(f"Placa: {placa}")
        print("=====================")
        registrar_historico("CADASTRO-TAG", placa, hora_entrada, None, 0)
        print("TAG cadastrada com sucesso!")
        
    elif opcao == "2":
        # Usar TAG existente
        tag = input("Digite o número da TAG: ").upper().strip()
        
        if tag not in veiculos_tag:
            print(f"ERRO: TAG {tag} não cadastrada!")
            return
        
        dados = veiculos_tag[tag]
        
        # Se veículo já está dentro, não registra novamente
        if dados.get('hora_entrada'):
            print(f"ERRO: Veículo com TAG {tag} já está dentro!")
            print(f"Entrada: {formatar_hora(dados['hora_entrada'])}")
            return
        
        # Registra entrada
        hora_entrada = time.time()
        dados['hora_entrada'] = hora_entrada
        
        print(f"\n*** ENTRADA REGISTRADA ***")
        print(f"TAG: {tag}")
        print(f"Placa: {dados['placa']}")
        print("=====================")
        registrar_historico("ENTRADA-TAG", dados['placa'], hora_entrada, None, 0)
        print("Entrada liberada! Bom trânsito!")

# ============================================
# 4 - SAÍDA POR TAG
# ============================================

def saida_tag():
    """Registra saída de veículo por TAG"""
    print("\n--- SAÍDA POR TAG ---")
    
    tag = input("Digite o número da TAG: ").upper().strip()
    
    if not tag:
        print("ERRO: TAG inválida!")
        return
    
    if tag not in veiculos_tag:
        print(f"ERRO: TAG {tag} não encontrada!")
        return
    
    dados = veiculos_tag[tag]
    
    # Verifica se veículo está dentro
    if not dados.get('hora_entrada'):
        print(f"ERRO: Veículo com TAG {tag} não está dentro!")
        return
    
    hora_entrada = dados['hora_entrada']
    hora_saida = time.time()
    placa = dados['placa']
    
    # Calcula tempo e valor
    tempo, valor = calcular_valor(hora_entrada, hora_saida)
    
    print("\n*** FATURA POR TAG ***")
    print(f"TAG: {tag}")
    print(f"Placa: {placa}")
    print(f"Entrada: {formatar_hora(hora_entrada)}")
    print(f"Saída: {formatar_hora(hora_saida)}")
    print(f"Tempo: {tempo} hora(s)")
    print(f"Valor: R$ {valor:.2f}")
    print("=====================")
    print("Fatura gerada! Valor será cobrado na próxima fatura.")
    
    # Limpa hora de entrada (veículo saiu)
    dados['hora_entrada'] = None
    
    print("\n*** CANCELA LIBERADA ***")
    registro = input("Pressione Enter para continuar...")
    registrar_historico("SAIDA-TAG", placa, hora_entrada, hora_saida, valor)

# ============================================
# 5 - ERROS E PROBLEMAS
# ============================================

def menu_erros():
    """Menu de erros e problemas"""
    print("\n*** ERROS E PROBLEMAS ***")
    print("1 - Perdeu o ticket")
    print("2 - TAG não funciona (sem sinal)")
    print("3 - Problema na cancela (não abre)")
    print("4 - Ticket e TAG ao mesmo tempo")
    
    opcao = input("Escolha o problema: ")
    
    if opcao == "1":
        tratar_ticket_perdido()
    elif opcao == "2":
        tratar_tag_sem_sinal()
    elif opcao == "3":
        tratar_problema_cancela()
    elif opcao == "4":
        tratar_ticket_e_tag()
    else:
        print("Opção inválida!")

def tratar_ticket_perdido():
    """Trata caso de ticket perdido"""
    print("\n--- TICKET PERDIDO ---")
    print("Procedimento: Informar dados do veículo")
    print("Cobrança mínima de 1 hora")
    
    placa = input("Digite a placa do veículo: ").upper().strip()
    
    if not placa:
        print("ERRO: Placa inválida!")
        return
    
    # Tenta encontrar o veículo
    if placa in veiculos_ticket:
        hora_entrada = veiculos_ticket[placa]
        
        print(f"\nVeículo encontrado!")
        print(f"Entrada: {formatar_hora(hora_entrada)}")
        
        # Cobra valor mínimo ou tempo real (o que for maior)
        hora_saida = time.time()
        tempo, valor = calcular_valor(hora_entrada, hora_saida)
        
        if valor < VALOR_MINIMO:
            valor = VALOR_MINIMO
            tempo = 1
            print("Por ter perdido o ticket, cobra-se taxa mínima.")
        
        print(f"\nValor a pagar: R$ {valor:.2f}")
        
        pagamento = input("Confirmar pagamento? (S/N): ").upper()
        
        if pagamento == "S":
            del veiculos_ticket[placa]
            print("Pagamento confirmado! Cancela liberada!")
            registrar_historico("TICKET-PERDIDO", placa, hora_entrada, hora_saida, valor)
        else:
            print("Pagamento não realizado!")
    else:
        # Veículo não encontrado, cobra taxa mínima
        print("\nVeículo não encontrado no sistema.")
        print("Cobrança taxa mínima de emergência.")
        
        hora_saida = time.time()
        valor = VALOR_MINIMO
        
        print(f"Valor a pagar: R$ {valor:.2f}")
        
        pagamento = input("Confirmar pagamento? (S/N): ").upper()
        
        if pagamento == "S":
            print("Pagamento confirmado! Cancela liberada!")
            # Não remove porque não estava registrado
            registrar_historico("TICKET-PERDIDO", placa, hora_saida, hora_saida, valor)
        else:
            print("Pagamento não realizado!")

def tratar_tag_sem_sinal():
    """Trata caso de TAG sem sinal"""
    print("\n--- TAG SEM SINAL ---")
    print("Verificações:")
    print("1 - Aproximar TAG novamente do leitor")
    print("2 - Verificar se TAG estádanificada")
    print("3 - Usar entrada manual (teclado)")
    
    # Simula verificação
    input("Pressione Enter para testar TAG novamente...")
    print("TAG testada. Verifique se há resposta do sistema.")
    
    print("\nSe ainda não funcionar:")
    print("- Use o modo manual (teclado)")
    print("- Chame o atendente")

def tratar_problema_cancela():
    """Trata problema na cancela"""
    print("\n--- PROBLEMA NA CANCELA ---")
    print("1 - Cancelas travadas")
    print("2 - Sensor não detecta veículo")
    print("3 - Operação manual necessária")
    
    print("\n*** AVISO ***")
    print("Cancela com problema!")
    print("Liberação manual em andamento...")
    print("Por favor, aguarde atendimento!")
    
    input("Pressione Enter para continuar...")

def tratar_ticket_e_tag():
    """Trata conflito de ticket e TAG"""
    print("\n--- TICKET E TAG SIMULTÂNEOS ---")
    print("ERRO: Sistema detectou ambos os modos!")
    print("Escolha uma opção:")
    print("1 - Usar apenas Ticket")
    print("2 - Usar apenas TAG")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        print("Modo Ticket selecionado.")
        print("Ignore a TAG e use o ticket.")
    elif opcao == "2":
        print("Modo TAG selecionado.")
        print("Desconsidere o ticket.")
    else:
        print("Opção inválida!")

# ============================================
# 6 - CONSULTAR HISTÓRICO
# ============================================

def consultar_historico():
    """Consulta histórico de operações"""
    print("\n--- HISTÓRICO DE OPERAÇÕES ---")
    
    if not historico:
        print("Nenhuma operação registrada!")
        return
    
    print(f"Total de operações: {len(historico)}")
    print("-" * 50)
    
    for i, op in enumerate(historico, 1):
        print(f"\n{i}. {op['tipo']}")
        print(f"   Placa: {op['placa']}")
        
        if op['entrada']:
            print(f"   Entrada: {formatar_hora(op['entrada'])}")
        
        if op['saida']:
            print(f"   Saída: {formatar_hora(op['saida'])}")
        
        if op['valor'] > 0:
            print(f"   Valor: R$ {op['valor']:.2f}")
    
    input("\nPressione Enter para continuar...")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Função principal do sistema"""
    print("\n" + "="*40)
    print("     SISTEMA DE CANCELA AUTOMÁTICA")
    print("     Estacionamento Simples")
    print("="*40)
    
    while True:
        mostrar_menu()
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            entrada_ticket()
        elif opcao == "2":
            saida_ticket()
        elif opcao == "3":
            entrada_tag()
        elif opcao == "4":
            saida_tag()
        elif opcao == "5":
            menu_erros()
        elif opcao == "6":
            consultar_historico()
        elif opcao == "0":
            print("\nSistema encerrado. Obrigado!")
            break
        else:
            print("\nOpção inválida!")

# Inicia o programa
if __name__ == "__main__":
    main()
