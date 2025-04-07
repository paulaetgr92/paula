class Professor:
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina  # Corrigido o erro de digitação

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "disciplina": self.disciplina}  # Agora vai funcionar corretamente

if __name__ == "__main__":
    prof = Professor(1, "João Silva", "Matemática")
    print(prof.to_dict())  # Deve imprimir: {'id': 1, 'nome': 'João Silva', 'disciplina': 'Matemática'}

