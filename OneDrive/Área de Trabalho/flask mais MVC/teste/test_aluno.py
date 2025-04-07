import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_listar_alunos(client):
    response = client.get('/alunos/')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_obter_aluno_existente(client):
    response = client.get('/alunos/1')
    assert response.status_code == 200
    assert "nome" in response.get_json()

def test_obter_aluno_inexistente(client):
    response = client.get('/alunos/999')
    assert response.status_code == 404

def test_criar_aluno(client):
    novo_aluno = {
        "nome": "Carlos",
        "idade": 17,
        "turma_id": 1,
        "data_nascimento": "2007-08-12",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 7.5,
        "media_final": 7.75
    }
    response = client.post('/alunos/', json=novo_aluno)
    assert response.status_code == 201
    assert "aluno" in response.get_json()

def test_atualizar_aluno(client):
    response = client.put('/alunos/1', json={"nome": "João Atualizado"})
    assert response.status_code == 200
    assert response.get_json()["aluno"]["nome"] == "João Atualizado"

def test_deletar_aluno(client):
    response = client.delete('/alunos/2')
    assert response.status_code == 200
