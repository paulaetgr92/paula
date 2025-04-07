from flask import Blueprint, jsonify, request
from model.turma import (
    get_turmas, turma_infos, cadastrar_turma,
    atualizar_turma, deletar_turma, TurmaNaoEncontrada
)

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/', methods=["GET"])
def listar_turmas():
    return jsonify(get_turmas())

@turma_bp.route('/<int:id>', methods=["GET"])
def obter_turma(id):
    try:
        return jsonify(turma_infos(id))
    except TurmaNaoEncontrada as e:
        return jsonify({"erro": str(e)}), 404

@turma_bp.route('/', methods=["POST"])
def criar_turma():
    try:
        dados = request.get_json()
        nova = cadastrar_turma(dados)
        return jsonify({"mensagem": "Turma cadastrada com sucesso!", "turma": nova}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@turma_bp.route('/<int:id>', methods=["PUT"])
def editar_turma(id):
    try:
        dados = request.get_json()
        turma_atualizada = atualizar_turma(id, dados)
        return jsonify({"mensagem": "Turma atualizada com sucesso!", "turma": turma_atualizada})
    except TurmaNaoEncontrada as e:
        return jsonify({"erro": str(e)}), 404

@turma_bp.route('/<int:id>', methods=["DELETE"])
def excluir_turma(id):
    try:
        resultado = deletar_turma(id)
        return jsonify(resultado)
    except TurmaNaoEncontrada as e:
        return jsonify({"erro": str(e)}), 404
