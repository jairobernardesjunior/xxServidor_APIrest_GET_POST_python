from flask import Flask, jsonify
from models.ngo import NGOEncoder
from extensions import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = NGOEncoder

@app.route('/')
def index():
    return '<h1>DADOS DE RETORNO DO CONSUMO DA API</h1>' + \
        '<p>Retorno do consumo da api_get</p>'

@app.route('/apiGet/v1/consulta/DB/atacado_varejo', methods=['GET'])
def list_all():
    return jsonify({'ngos': db})

app.run()