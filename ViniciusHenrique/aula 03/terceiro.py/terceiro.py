


# # def saudaçâo(nome):
# #     return f"OLá, {nome}! "

# # mensagem = saudaçâo("Vinicius")
# # print(mensagem)

# # nome = input("Seu nome:  ")
# # idade = int(input("Sua idade:  "))# Converte pa
# # print(f"{nome} tem {idade} anos.")

# # Cauculo de notas por semestre onde tera duas notas formativas e uma nota somativa para encerrar o semestre 


# print ("Seu primeiro semestre foi")
# nota1 = int(input(" sua nota 1 foi em um valor de:   \n"))
# nota2 = int(input(" sua nota 2 foi em um valor de:   \n"))
# nota3 = int(input(" sua nota 3 foi em um valor de:   \n"))
# ntotal = ((nota1 + nota2 + nota3) /3)
# print("A media do primeiro semestre"  ,ntotal)

# print ("seu segundo semestre foi")
# nota1 = int(input(" sua nota 1 foi em um valor de:   \n"))
# nota2 = int(input(" sua nota 2 foi em um valor de:   \n"))
# nota3 = int(input(" sua nota 3 foi em um valor de:   \n"))
# print((nota1 + nota2 + nota3) /3)
# print("A media do segundo semestre"  ,ntotal)

# print(" Realatorio de notas")
# print("Media do primeiro semestre" , ntotal)
# print("Media do segundo semestre" , ntotal)

# boas_vindas("Ana" , "Desenvolvedora")
# boas_vindas("Carlos" , "Gerente")

# def configurar_conexao(servidor , porta=8080):
#     print(f"conectando a {servidor} na porta {porta}...")

# configurar_conexao("192.168.1.1")
# configurar_conexao("10.0.0.1" , 3000)
# configurar_conexao("192.168.1.2")
# vinj

# nome = input('Meu nome é  \n')
# curso = input('Meu curso é  \n')
# nascimento =int (input('minha data de nascimento é  \n'))
# ano = int (input("Digite o ano: \n"))
# idade = (ano - nascimento)
# print("Sua idade é:" , idade)

# print("Nota fiscal")
# conta = int(input("digite o valor da sua conta   \n"))
# porcentagem = int(input("o valor da porcentagem e de:" ))
# total = (conta / porcentagem) + conta
# print("O valor da sua compra foi de" , total)

# print("Um sistema sucessor e antecessor")
# numero = int(input("digite o numero dessejado   \n"))
# print ("O antecessor é \n" , numero -1 )
# print ("O sucessor é \n" , numero + 1)

print("Bem vindo a nossa loja de livros")
livros = int(input("digite o valor dos livros   \n"))
quantidade= int(input("Qual a quantidade de livros comprados:" ))
total = (livros - (livros * quantidade  /5))
print("O valor da sua compra foi de" , total)


print("\n=== Cálculo da Média de Lista com Tratamento de ValueError ===")

try:
    N = int(input("Digite o número de elementos da lista: "))
    if N <= 0:
        print("Erro: O número deve ser positivo.")
    else:
        numeros = []
        for i in range(N):
            try:
                num = int(input(f"Digite o número {i+1}: "))
                numeros.append(num)
            except ValueError:
                print(f"Erro no número {i+1}: Digite um número inteiro válido.")
                # Continue para permitir input correto ou ajustar lógica se necessário
        
        if numeros:
            media = sum(numeros) / len(numeros)
            print(f"A média dos números {numeros} é: {media:.2f}")
        else:
            print("Nenhum número válido foi inserido.")
except ValueError:
    print("Erro: Digite um número inteiro válido para o tamanho da lista.")
