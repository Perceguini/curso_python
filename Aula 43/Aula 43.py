perguntas = {
    'pergunta': {
        'pergunta': 'Quanto é 2 + 2?',
        'resposta': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },

    'pergunta2': {
        'pergunta': 'Quanto é 3*2?',
        'resposta': {'a': '1', 'b': '3', 'c': '6', },
        'resposta_certa': 'c',
    },

    'pergunta3': {
        'pergunta': 'Quanto é 5*6?',
        'resposta': {'a': '30', 'b': '3', 'c': '65', },
        'resposta_certa': 'a',
    },

    'pergunta4': {
        'pergunta': 'Quanto é 1-1?',
        'resposta': {'a': '100', 'b': '1', 'c': '0', },
        'resposta_certa': 'c',
    }

}

respostas_certas = 0
for pk, pv, in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Excolha uma das opções a baixo:')
    for rk, rv in pv['resposta'].items():
        print(f'{[rk]}: {rv}')

    resposta_usuario = input('Alternativa:  ')

    if resposta_usuario == pv['resposta_certa']:
        print('\033[94mVocê acertou!\033[0m')
        print()
        respostas_certas += 1
    else:
        print('\033[91mVocê errou :(.\033[0m')

        print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%.')
