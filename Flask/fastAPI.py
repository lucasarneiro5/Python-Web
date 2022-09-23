from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "refrigerante", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "agua", "preco_unitario": 3, "quantidade": 4},
    3: {"item": "H2O", "preco_unitario": 4, "quantidade": 5},

}

@app.get("/")
def home():
    return "FastAPI is online"

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID venda inexistente!"}