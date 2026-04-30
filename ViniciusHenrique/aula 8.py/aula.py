# # # # Clean code - aula 8
# # # # Para que usar?
# # # # Como usar?
# # # print("Clean code - Aula 8")
# # # aula = 8
# # # print(F"Estamos na aula {aula} de Clean Code")

# # # # Manipulação de arquivos de texto
# # # texto = " Python "
# # # print(texto.strip().upper ()) # Phyton
# # # print(texto.strip().lower())
# # # print(texto.strip().capitalize ()) # Phyton
# # # print(texto.strip().title())
# # # print(texto.strip().replace ()) # Phyton
# # # print(texto.strip().split())

# # # # # #Escrevendo
# with open("temperatura.txt", "w") as arquivo:
#  arquivo.write("Estudar Phyton hoje!")
# arquivo.write("\nler sobre Clean code")

# # #  Lendo 
# with open("temperatura.txt", "r")as arquivo:
#  conteudo = arquivo.read()
# print(conteudo)

# # # # Execução de comando
# # import os
# # # # print(os. getcwd)

# # # print(os.listdir())
# # # print(os.listdir(".."))
# # # print(os.listdir("..\\.."))
# # # print(os.listdir("C:\\"))
# # # print(os.listdir("C:\\Users"))
# # # print(os.listdir("C:\\Users\\Public"))


# # # os.mkdir("Nova_pasta")
# # # os.rename("nova_pasta", "pasta_renomeada")
# os.rmdir("pasta_renomeada")

# # # 1  Crie um scrpit que mostre o caminnho da pasta atual

# # caminho_atual = os.getcwd()
# # print(f"Caminho da pasta atual: {caminho_atual}")

# # #2 liste os arquivos da pasta atual

# # print(os.listdir())

# # #3 Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim exclua a pasta
# # os.mkdir("projetos")
# # os.rename("projetos", "meus_projetos")
# # os.rmdir("Meus_projetos")

# #4 crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteudo do arquivo e exiba na tela

# ##Escrevendo
# # with open("log.txt", "w") as arquivo:
# #   arquivo.write("\nlog de atividades")

# #  # Lendo 
# # with open("log.txt", "r")as arquivo:
# #  conteudo = arquivo.read()
# # print(conteudo)

# # # Crie um dicionario com as informações sobre uma pessoa e acesse usando uma chave
# # pessoa = {
# #  "nome":"Alice",
# #  "idade":  30,
# # "cidade": "São Paulo",
# # "Profissão": "Engenharia"
# # }
# # print(pessoa["nome"],["idade"])
# # pessoa2 = {
# #  "nome":"Vinicius",
# #  "idade":   16,
# # "cidade": "São Paulo",
# # "Profissão": "Ti"
# # }

# # print(pessoa2["nome"], pessoa["idade"])

# # # 6
# # with open("desliga.bat") as desligar:
# #     desligar.write("shutdown")

# # with open("desliga.bat", "w") as desligar:
# #     desligar.write("shutdown -s -t 3600 -c\"Desligamento")


# # with open("desliga.bat", "r") as desligar:
# #     conteudo = desligar.read()
# #     print(conteudo)

# # Exercicio 7: criar arquivo de backup simples
# # Escreva script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteudo de 'notas.txt" e escrever no novo arquivo

# import os

# with open("notas.txt", "r") as notas:
#     conteudo = notas.read()

# with open("notas_backup.txt", "w") as backup:
#     backup.write(conteudo)

# pasta = os.listdir()
# for arquivo in pasta:
#     if arquivo.endswith(".temp"):
#         os.remove(arquivo)
#         print(F"Arquivo {arquivo} excluido.")
#         print("Limpeza de arquivos concluida.")

# Criar um script de monitoramento de temperatura, escreva um script que monitore a temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura. txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°

import os

with open("temperatura.txt", "r") as f:
    temp = float(f.read().strip())
print(f"Temperatura: {temp}°C")
if temp > 70:
    print("ALERTA: Temperatura alta!")
else:
    print("Temperatura OK.")