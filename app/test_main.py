import pytest
from fastapi.testclient import TestClient
from main import app
import helpconfig

client = TestClient(app)

def test_soma():
    response = client.post("/calcular", json={
        "valor1": 10,
        "valor2": 5,
        "operacao": "soma"
    })
    assert response.status_code == 200
    assert response.json() == {"resultado": 15}

def test_subtracao():
    response = client.post("/calcular", json={
        "valor1": 20,
        "valor2": 8,
        "operacao": "subtracao"
    })
    assert response.status_code == 200
    assert response.json() == {"resultado": 12}

def test_multiplicacao():
    response = client.post("/calcular", json={
        "valor1": 7,
        "valor2": 6,
        "operacao": "multiplicacao"
    })
    assert response.status_code == 200
    assert response.json() == {"resultado": 42}

def test_divisao():
    response = client.post("/calcular", json={
        "valor1": 12,
        "valor2": 3,
        "operacao": "divisao"
    })
    assert response.status_code == 200
    assert response.json() == {"resultado": 4.0}

def test_divisao_por_zero():
    response = client.post("/calcular", json={
        "valor1": 10,
        "valor2": 0,
        "operacao": "divisao"
    })
    assert response.status_code == 200
    assert response.json()["resultado"] == "Erro: divisão por zero"

def test_operacao_invalida():
    response = client.post("/calcular", json={
        "valor1": 5,
        "valor2": 5,
        "operacao": "raiz"
    })
    assert response.status_code == 200
    assert response.json()["resultado"] == "Operação inválida"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)