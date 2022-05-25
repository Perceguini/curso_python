"""
Dicionarios em python.
"""

clientes = {
    'cliente1': {
        'nome': 'Leticia',
        'sobrenome': 'Perceguini'
    },
    'cliente2': {
        'nome': 'Kairo',
        'sobrenome': 'Amorim'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibido {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
