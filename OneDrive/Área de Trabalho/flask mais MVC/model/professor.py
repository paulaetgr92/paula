professores = [
    {"id": 1, "nome": "Carlos", "idade": 40, "materia": "Matemática", "observacoes": "Doutorado em Álgebra"},
    {"id": 2, "nome": "Ana", "idade": 35, "materia": "História", "observacoes": "Especialista em História Antiga"},
]

class ProfessorNaoEncontrado(Exception):
    pass

def get_professores():
    return professores


def professor_infos(id):
        for professor in professores:
            if professor["id"] == id:
                return professor
        raise ProfessorNaoEncontrado(f"Professor com ID {id} não encontrado.")



professores = []

def cadastrar_professor(dados):
    novo = {
        "id": len(professores) + 1,
        "nome": dados["nome"],
        "materia": dados["materia"]
    }
    professores.append(novo)
    return novo



def atualizar_professor(id,dados):
        for professor in professores:
            if professor["id"] == id:
                professor["nome"] = dados.get("nome", professor["nome"])
                professor["idade"] = dados.get("idade", professor["idade"])
                professor["materia"] = dados.get("materia", professor["materia"])
                professor["observacoes"] = dados.get("observacoes", professor["observacoes"])
                return professor
            raise ProfessorNaoEncontrado (f"Professor com ID {id} não encontrado.")
        
def deletar_professor(id):
        for professor in professores:
            if professor["id"] == id:
                professores.remove(professor)
                return {"mensagem": f"Professor com id {id} removido com sucesso."}
            raise ProfessorNaoEncontrado(f"Prcom ID {id} não encontrado.")