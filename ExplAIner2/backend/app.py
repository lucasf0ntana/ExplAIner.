import os
#from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

import backend.models.database as d
from backend.controllers.aluno_controller import aluno_controller


def create_app():
    #load_dotenv()

    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/explainer")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    d.db.init_app(app)

    app.register_blueprint(aluno_controller)

    @app.get("/")
    def home():
        return jsonify({
            "mensagem": "API Flask + SQLAlchemy - Sistema de Gamificação Educacional",
            "rotas": {
                "alunos": {
                    "listar": "GET /alunos",
                    "buscar": "GET /alunos/<id>",
                    "criar": "POST /alunos",
                    "atualizar": "PUT /alunos/<id>",
                    "deletar": "DELETE /alunos/<id>"
                }
            }
        })

    with app.app_context():
        d.db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "True") == "True"
    app.run(debug=debug)