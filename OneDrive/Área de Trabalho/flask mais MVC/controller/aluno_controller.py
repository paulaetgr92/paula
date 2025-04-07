from flask import Blueprint, jsonify, request
from model.aluno import (
    get_alunos, aluno_infos, cadastrar_aluno,
    atualizar_aluno, deletar_aluno, AlunoNaoEncontrado
)

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/', methods=["GET"])
def listar_alunos():
    return jsonify(get_alunos())

@aluno_bp.route('/<int:id>', methods=["GET"])
def obter_aluno(id):
    try:
        return jsonify(aluno_infos(id))
    except AlunoNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404

@aluno_bp.route('/', methods=["POST"])
def criar_aluno():
    try:
        dados = request.get_json()
        novo = cadastrar_aluno(dados)
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "aluno": novo}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@aluno_bp.route('/<int:id>', methods=["PUT"])
def editar_aluno(id):
    try:
        dados = request.get_json()
        aluno_atualizado = atualizar_aluno(id, dados)
        return jsonify({"mensagem": "Aluno atualizado com sucesso!", "aluno": aluno_atualizado})
    except AlunoNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404

@aluno_bp.route('/<int:id>', methods=["DELETE"])
def excluir_aluno(id):
    try:
        resultado = deletar_aluno(id)
        return jsonify(resultado)
    except AlunoNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404
