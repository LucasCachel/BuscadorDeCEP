import requests

def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return {
                'cep': data['cep'],
                'logradouro': data['logradouro'],
                'complemento': data['complemento'],
                'bairro': data['bairro'],
                'localidade': data['localidade'],
                'uf': data['uf'],
                'ibge': data['ibge'],
                'gia': data['gia'],
                'ddd': data['ddd'],
                'siafi': data['siafi']
            }
    return None

def main():
    cep = input('Digite o CEP que deseja pesquisar: ')
    endereco = buscar_cep(cep)

    if endereco:
        print('\nInformações do endereço:')
        for chave, valor in endereco.items():
            print(f'{chave}: {valor}')
    else:
        print('CEP inválido ou não encontrado.')

if __name__ == "__main__":
    main()
