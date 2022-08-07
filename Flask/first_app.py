from flask import Flask, render_template

app = Flask(__name__)

# Criar a pagina do site - Toda pagina tem:
# Route -> O caminho, ou o link do site (rota), ex: https://github.com/lucasarneiro5 
# Função -> Oq vc quer exibir na página

@app.route("/") # -> Decorator: Tem objetivo de atribuir uma nova funcionalidade a funcao que vem logo embaixo
# A funcao abaixo vai ser exibida na home page
def homepage():
    return render_template("homepage.html")

# Adicionar contatos
@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

# Criar usuarios
@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__== "__main__": # Executa o codigo abaixo. Se for importado por outro arquivo, nao vai importar oq está abaixo.
    app.run(debug=True)

# Deploy em um servidor