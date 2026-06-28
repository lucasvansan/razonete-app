from accounting_classes import Razonete
from flask import Flask, jsonify, request

app = Flask(__name__)
razonetes = []


def serialize_razonete(razonete: Razonete, razonete_id: int):
    return {
        'id': razonete_id,
        'nome_conta': razonete.nome_conta,
        'natureza_contabil': razonete.natureza_contabil,
        'livro_razao': razonete.livro_razao.to_dict(orient='records'),
        'totalizador': razonete.totalizador(),
    }

@app.get('/')
def index():
    return jsonify({'message': 'Razonete API'})


@app.get('/api/razonetes')
def list_razonetes():
    return jsonify([serialize_razonete(razonete, index + 1) for index, razonete in enumerate(razonetes)])


@app.post('/api/razonetes')
def create_razonete():
    payload = request.get_json(silent=True) or {}
    nome_conta = payload.get('nome_conta') or f'Razonete {len(razonetes) + 1}'
    natureza_contabil = payload.get('natureza_contabil', 'Ativo')

    razonete = Razonete(nome_conta, natureza_contabil)
    razonetes.append(razonete)

    return jsonify(serialize_razonete(razonete, len(razonetes))), 201
# a = Razonete('Passivo',lanc_credito={'1a':2000})
# a.saldo()
