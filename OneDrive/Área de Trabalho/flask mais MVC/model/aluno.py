
alunos = [
    {"id": 1, "nome": "João", "idade": 16, "turma_id": 1, "data_nascimento": "2008-05-12", 
     "nota_primeiro_semestre": 7.5, "nota_segundo_semestre": 8.0, "media_final": 7.75},
    {"id": 2, "nome": "Mariana", "idade": 15, "turma_id": 2, "data_nascimento": "2009-07-20",
     "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 8.5, "media_final": 8.75}
]

class AlunoNaoEncontrado(Exception):
    pass

def get_alunos():
    return alunos

def aluno_infos(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return aluno
    raise AlunoNaoEncontrado(f"Aluno com ID {id} não encontrado.")

def cadastrar_aluno(novo_aluno):
    for aluno in alunos:
        if (aluno["nome"].lower() == novo_aluno["nome"].lower() and
            aluno["idade"] == novo_aluno["idade"] and
            aluno["turma_id"] == novo_aluno["turma_id"] and
            aluno["data_nascimento"] == novo_aluno["data_nascimento"] and
            aluno["nota_primeiro_semestre"] == novo_aluno["nota_primeiro_semestre"] and
            aluno["nota_segundo_semestre"] == novo_aluno["nota_segundo_semestre"] and
            aluno["media_final"] == novo_aluno["media_final"]):
            raise Exception("Aluno já cadastrado")

    novo_aluno["id"] = len(alunos) + 1
    alunos.append(novo_aluno)
    return novo_aluno


def atualizar_aluno(id, dados):
    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = dados.get("nome", aluno["nome"])
            aluno["idade"] = dados.get("idade", aluno["idade"])
            aluno["turma_id"] = dados.get("turma_id", aluno["turma_id"])
            aluno["data_nascimento"] = dados.get("data_nascimento", aluno["data_nascimento"])
            aluno["nota_primeiro_semestre"] = dados.get("nota_primeiro_semestre", aluno["nota_primeiro_semestre"])
            aluno["nota_segundo_semestre"] = dados.get("nota_segundo_semestre", aluno["nota_segundo_semestre"])
            aluno["media_final"] = dados.get("media_final", aluno["media_final"])
            return aluno
    raise AlunoNaoEncontrado(f"Aluno com ID {id} não encontrado.")

    

def deletar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return {"mensagem": f"Aluno com id {id} removido com sucesso."}
    raise AlunoNaoEncontrado(f"Aluno com ID {id} não encontrado.")
