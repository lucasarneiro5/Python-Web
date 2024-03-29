from flask import Flask, render_template, request

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Aventura', 'GameBoy')
jogo2 = Jogo('Pokemon Go', 'RPG', 'Mobile')
jogo3 = Jogo('R6', 'FPS', 'PC')
lista = [jogo1, jogo2, jogo3]    

@app.route('/')
def index():
    #lista = ['Tetris', 'Super Mario', 'Pokemon']
    return render_template('lista.html', titulo='Jogos', jogos=lista);

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
   nome = request.form['nome']
   categoria = request.form['categoria']
   console = request.form['console']
   jogo = Jogo(nome, categoria, console)
   lista.append(jogo)
   return render_template('lista.html', titulo='Jogos', jogos=lista) 

app.run(debug=True)