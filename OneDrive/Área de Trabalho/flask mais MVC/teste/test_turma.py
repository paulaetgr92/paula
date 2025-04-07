import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_listar_turmas(client):
    response = client.get('/turmas/')
    assert response.status_code == 200

def test_criar_turma(client):
    response = client.post('/turmas/', json={
        "nome": "1º Ano A", "turno": "Manhã"
    })
    assert response.status_code == 201
