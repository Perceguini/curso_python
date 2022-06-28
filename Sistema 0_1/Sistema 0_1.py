import os
from random import randint

"""
---Sistema da LeLe---

1 - Menu CPF
2 - Menu Pessoas
0 - Sair do sistema

Opção: xx
---------------------

------Menu CPF-------

1 - Validar CPF
2 - Gerador de CPF
0 - Voltar

Opção: xx
---------------------

----Menu Pessoas-----

1 - Listar Pessoas
2 - Salvar Pessoa
3 - Editar Pessoa
4 - Excluir Pessoa
0 - Voltar

Opção: xx
---------------------
"""

usuario = input('Digite o seu usuario:  ')
senha = input('Digite a senha: ')

menu_principal = """---Sistema da LeLe---

1 - Menu CPF
2 - Menu Pessoas
3 - Jogos
0 - Sair do sistema
"""

menu_cpf = """------Menu CPF-------

1 - Validar CPF
2 - Gerador de CPF
0 - Voltar
"""
menu_pessoas = """----Menu Pessoas-----

1 - Listar Pessoas
2 - Salvar Pessoa
3 - Editar Pessoa
4 - Excluir Pessoa
0 - Voltar

Opção: xx
"""

jogos = """jogos_de_alternativas

1 - Jogo de alternativas
"""

if len(senha) <= 6:
    print('Senha incoreta, digite pelo menos 6 caracteres.')
else:

    print('Usuario logado')

pessoas = []

# While do menu principal
while True:
    print(menu_principal)
    opcao = input("Opção: ")
    os.system('cls')

    if opcao == "1":
        # While do menu CPF
        while True:
            print(menu_cpf)
            opcao_cpf = input('Opção: ')
            print('------')
            os.system('cls')

            if opcao_cpf == "1":
                print('Validador de CPF.')
                cpf = input('Digite um CPF:  ')
                cpf_novo = cpf[:-2]
                reverso = 10
                total = 0
                for index in range(19):
                    if index > 8:
                        index -= 9
                    total += int(cpf_novo[index]) * reverso

                    reverso -= 1
                    if reverso < 2:
                        reverso = 11
                        d = 11 - (total % 11)

                        if d > 9:
                            d = 0
                        total = 0
                        cpf_novo += str(d)
                if cpf == cpf_novo:
                    print('CPF válido')
                else:
                    print('CPF inválido')
                input("Digite ENTER para continuar...")

            elif opcao_cpf == "2":
                os.system('cls')
                print(" Gerador de CPF")

                numero = str(randint(100000000, 999999999))
                novo_cpf = numero
                reverso = 10
                total = 0
                for index in range(19):
                    if index > 8:
                        index -= 9
                    total += int(novo_cpf[index]) * reverso
                    reverso -= 1
                    if reverso < 2:
                        reverso = 11
                        d = 11 - (total % 11)
                        if d > 9:
                            d = 0
                        total = 0
                        novo_cpf += str(d)

                print(novo_cpf)
                input("Digite ENTER para continuar...")
                os.system('cls')

            elif opcao_cpf == '0':
                break

    elif opcao == "2":
        while True:
            print(menu_pessoas)
            opcao_pessoas = input('Opção: ')
            print('----')
            # Opção de Listar pessoas da lista
            if opcao_pessoas == '1':
                if len(pessoas) > 0:
                    for indice, pessoa in enumerate(pessoas):
                        print(f"{indice} - {pessoa}")
                else:
                    print("Não há pessoas cadastradas")
                input("Digite ENTER para continuar...")
                os.system('cls')


            # Opção de salvar pessoa na lista
            elif opcao_pessoas == '2':
                pessoas.append(input("Digite o nome da pessoa: "))
                input("Digite ENTER para continuar...")
                os.system('cls')


            # Opção de editar pessoa da lista
            elif opcao_pessoas == '3':
                while True:
                    print(menu_pessoas)
                    opcao_pessoas = input('Opção: ')
                    print('----')

                if len(pessoas) > 0:
                    for indice, pessoa in enumerate(pessoas):
                        print(f"{indice} - {pessoa}")
                    indice_pessoa = int(input("Qual pessoa? "))
                    pessoas[indice_pessoa] = input("Nome: ")
                else:
                    print("Não há pessoas cadastradas")
                input("Digite ENTER para continuar...")
                os.system('cls')


            # Opção de Excluir pessoa da lista
            elif opcao_pessoas == '4':
                if len(pessoas) > 0:
                    for indice, pessoa in enumerate(pessoas):
                        print(f"{indice} - {pessoa}")
                    pessoas.pop(int(input("Digite o código da pessoa que será excluída: ")))
                else:
                    print("Não há pessoas cadastradas")
                input("Digite ENTER para continuar...")
                os.system('cls')

            elif opcao_pessoas == '0':
                break

    elif opcao == "0":
        print("Saindo do sistema da LeLe. xauuu.....")
        break
