import pandas as pd
from flask import Flask, jsonify
import warnings
warnings.filterwarnings("ignore")

# Creating API
app = Flask(__name__)

# Construir Funcionalidades
@app.route('/')
def homepage():
    return 'This API is online!'

@app.route('/contatos')
def contatos():
    return 'This is the contact page'

@app.route('/transactionshistory')
def bank_transactions():
    tabela = pd.read_csv('BaseRazao.csv', sep=';')
    total_vendas = tabela['Valor'].sum()
    total_vendas = float(total_vendas)
    tabela['DataTransacao'] = pd.to_datetime(tabela['DataTransacao'])
    data_json = tabela['DataTransacao'].to_json(orient='records', date_format='iso', date_unit='s')
    #, 'date_transact': [data_json] 'total_sale': total_vendas
    answer = {'date_transact': [data_json], 'total_sale': [total_vendas]}
    return jsonify(answer)

# Rodar a API
app.run()