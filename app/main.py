from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Operacao(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/calcular")
def calcular(req: Operacao):
    op = req.operacao.lower()

    if op == "soma":
        resultado = req.valor1 + req.valor2
    elif op == "subtracao":
        resultado = req.valor1 - req.valor2
    elif op == "multiplicacao":
        resultado = req.valor1 * req.valor2
    elif op == "divisao":
        if req.valor2 == 0:
            resultado = "Erro: divisão por zero"
        else:
            resultado = req.valor1 / req.valor2
    else:
        resultado = "Operação inválida"

    return {"resultado": resultado}