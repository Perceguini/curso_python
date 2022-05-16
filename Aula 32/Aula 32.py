import os

while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    total = 0

    reverso = 10
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

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')

    # É utilizado o Input para esperar o 'ENTER' do usuário antes de executar o próximo comando
    # e então, é utilizada a biblioteca 'os' para executar comandos do sistema, nesse caso o 'cls'
    # para limpar o terminal
    input("Pressione ENTER para continuar...")
    os.system('cls')
