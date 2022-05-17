from random import randint

numero = str(randint(100000000, 999999999))

# Elimina os dois últimos digitos do CPF
# Contador reverso.
novo_cpf = numero
total = 0

# Loop do CPF
# Primeiro índice vai de 0 a 9, são ps 9 primeiros digitos do CPF
for index in range(19):
    if index > 8:
        index -= 9

    # Valor total da multiplicação
    total += int(novo_cpf[index]) * reverso

    # Decrementa o contador reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        # Se o digito for > que 9 é 0
        if d > 9:
            d = 0
        total = 0  # Zera o total
        novo_cpf += str(d)  # Concatena o digito gerado no novo CPF

print(novo_cpf)
