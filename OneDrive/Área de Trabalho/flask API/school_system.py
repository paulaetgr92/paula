from flask import Flask, jsonify, request
import sys
import os

# Adiciona o diretório 'model' ao caminho de importação
sys.path.append(os.path.abspath("model"))

# Importa as classes de Professor, Aluno e Turma
from professor import Professor
from aluno import Aluno
from turma import Turma

app = Flask(__name__)

# Dados iniciais
professores = [Professor(1, "João Silva", "Matemática"), Professor(2, "Maria Souza", "Português")]
alunos = [Aluno(1, "Carlos Silva", 19), Aluno(2, "Ana Costa", 20)]
turmas = [Turma(1, 1, [1, 2], "Turma A"), Turma(2, 2, [1], "Turma B")]

# Função auxiliar para buscar um item por ID
def buscar_por_id(lista, id):
    return next((item for item in lista if item.id == id), None)

# Tratamento de erros
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"erro": "Recurso não encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"erro": "Erro interno no servidor"}), 500

# Rotas para Professores
@app.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify([prof.to_dict() for prof in professores]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/professores/id/<int:id>', methods=['GET'])
def obter_professor(id):
    try:
        professor = buscar_por_id(professores, id)
        if professor:
            return jsonify(professor.to_dict()), 200
        return jsonify({"erro": "Professor não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/professores', methods=['POST'])
def cadastrar_professor():
    try:
        dados = request.json
        if not dados.get("nome") or not dados.get("disciplina"):
            return jsonify({"erro": "Nome e disciplina são obrigatórios"}), 400
        novo_professor = Professor(len(professores) + 1, dados["nome"], dados["disciplina"])
        professores.append(novo_professor)
        return jsonify(novo_professor.to_dict()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rotas para Alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        return jsonify([aluno.to_dict() for aluno in alunos]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/alunos/id/<int:id>', methods=['GET'])
def obter_aluno(id):
    try:
        aluno = buscar_por_id(alunos, id)
        if aluno:
            return jsonify(aluno.to_dict()), 200
        return jsonify({"erro": "Aluno não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    try:
        dados = request.json
        if not dados.get("nome") or not dados.get("idade"):
            return jsonify({"erro": "Nome e idade são obrigatórios"}), 400
        novo_aluno = Aluno(len(alunos) + 1, dados["nome"], dados["idade"])
        alunos.append(novo_aluno)
        return jsonify(novo_aluno.to_dict()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rotas para Turmas
@app.route('/turmas', methods=['GET'])
def listar_turmas():
    try:
        return jsonify([turma.to_dict() for turma in turmas]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/turmas/id/<int:id>', methods=['GET'])
def listar_turma_por_id(id):
    try:
        turma = buscar_por_id(turmas, id)
        if turma:
            return jsonify(turma.to_dict()), 200
        return jsonify({"erro": "Turma não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/turmas', methods=['POST'])
def cadastrar_turma():
    try:
        dados = request.json
        if not dados.get("professor_id") or not dados.get("alunos"):
            return jsonify({"erro": "Professor e alunos são obrigatórios"}), 400
        nova_turma = Turma(len(turmas) + 1, dados["professor_id"], dados["alunos"], dados["nome"])
        turmas.append(nova_turma)
        return jsonify(nova_turma.to_dict()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Atualização de Professores, Alunos e Turmas
@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        professor = buscar_por_id(professores, id)
        if not professor:
            return jsonify({"erro": "Professor não encontrado"}), 404
        
        dados = request.json
        professor.nome = dados.get("nome", professor.nome)
        professor.disciplina = dados.get("disciplina", professor.disciplina)
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = buscar_por_id(alunos, id)
        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404
        
        dados = request.json
        aluno.nome = dados.get("nome", aluno.nome)
        aluno.idade = dados.get("idade", aluno.idade)
        return jsonify(aluno.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        turma = buscar_por_id(turmas, id)
        if not turma:
            return jsonify({"erro": "Turma não encontrada"}), 404
        
        dados = request.json
        turma.professor_id = dados.get("professor_id", turma.professor_id)
        turma.alunos = dados.get("alunos", turma.alunos)
        turma.nome = dados.get("nome", turma.nome)
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
