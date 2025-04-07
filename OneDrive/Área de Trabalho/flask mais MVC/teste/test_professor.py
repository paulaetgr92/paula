import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_listar_professores(client):
    response = client.get('/professores/')
    assert response.status_code == 200

def test_criar_professor(client):
    response = client.post('/professores/', json={
        "nome": "Ana", "disciplina": "Matemática"
    })
    assert response.status_code == 201
