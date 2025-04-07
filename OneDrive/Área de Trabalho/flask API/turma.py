class Turma:
    def __init__(self, id, professor_id, alunos, nome):
        self.id = id
        self.professor_id = professor_id
        self.alunos = alunos  # Lista de IDs de alunos
        self.nome = nome

    def to_dict(self):
        return {"id": self.id, "professor_id": self.professor_id, "alunos": self.alunos, "nome": self.nome}
