from flask import Blueprint, jsonify, request
from model.professor import (
    get_professores, professor_infos, cadastrar_professor,
    atualizar_professor, deletar_professor, ProfessorNaoEncontrado
)

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/', methods=["GET"])
def listar_professores():
    return jsonify(get_professores())

@professor_bp.route('/<int:id>', methods=["GET"])
def obter_professor(id):
    try:
        return jsonify(professor_infos(id))
    except ProfessorNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404

@professor_bp.route('/', methods=["POST"])
def criar_professor():
    try:
        dados = request.get_json()
        novo = cadastrar_professor(dados)
        return jsonify({"mensagem": "Professor cadastrado com sucesso!", "professor": novo}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@professor_bp.route('/<int:id>', methods=["PUT"])
def editar_professor(id):
    try:
        dados = request.get_json()
        professor_atualizado = atualizar_professor(id, dados)
        return jsonify({"mensagem": "Professor atualizado com sucesso!", "professor": professor_atualizado})
    except ProfessorNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404

@professor_bp.route('/<int:id>', methods=["DELETE"])
def excluir_professor(id):
    try:
        resultado = deletar_professor(id)
        return jsonify(resultado)
    except ProfessorNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404
