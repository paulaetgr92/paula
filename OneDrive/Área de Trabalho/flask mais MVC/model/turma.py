turmas = [
    {"id": 1, "descricao": "Turma A - Ensino Médio", "professor_id": 1, "ativo": True},
    {"id": 2, "descricao": "Turma B - Fundamental", "professor_id": 2, "ativo": True},
]

class TurmaNaoEncontrada(Exception):
    pass


def get_turmas():
    return turmas

def turma_infos(id):
     for turma in turmas:
            if turma['id'] == id:
                return turma
            raise TurmaNaoEncontrada(f"Turma com ID {id} não encontrado.")


def cadastrar_turma(nova_turma):
    for turma in turmas:
            if (turma["descricao"].lower() == nova_turma["descricao"].lower() and
                turma["professor_id"] == nova_turma["professor_id"] and
                turma["ativo"] == nova_turma["ativo"]):
                 raise Exception ("Turma já cadastrada")
            nova_turma["id"] = len(turmas) + 1
            turmas.append(nova_turma)

def atualizar_turma(id, dados):
        
        for turma in turmas:
            if turma["id"] == id:
                turma["descricao"] = dados.get("descricao", turma["descricao"])
                turma["professor_id"] = dados.get("professor_id", turma["professor_id"])
                turma["ativo"] = dados.get("ativo", turma["ativo"])
                return turma
            raise TurmaNaoEncontrada (f"Turma com ID {id} não encontrado.")
def deletar_turma(id):
        for turma in turmas:
            if turma["id"] == id:
                turmas.remove(turma)
                return({"mensagem": f"Turma com id {id} removida com sucesso."})
            raise TurmaNaoEncontrada(f"Professorcom ID {id} não encontrado.")
