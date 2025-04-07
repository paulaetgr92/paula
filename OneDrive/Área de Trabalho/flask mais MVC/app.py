from flask import Flask
from controller.aluno_controller import aluno_bp
from controller.professor_controller import professor_bp
from controller.turma_controller import turma_bp

app = Flask(__name__)


app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")

@app.route("/")
def home():
    return {
        "mensagem": "API Flask MVC - Alunos, Professores e Turmas",
        "endpoints": {
            "alunos": "/alunos",
            "professores": "/professores",
            "turmas": "/turmas"
        }
    }

if __name__ == "__main__":
    app.run(debug=True)
