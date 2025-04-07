class Aluno:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "idade": self.idade}
