from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    endereco = None

    if request.method == 'POST':
        cep = request.form['cep']
        endereco = buscar_cep(cep)

    return render_template('index.html', endereco=endereco)

if __name__ == '__main__':
    app.run(debug=True)
