"""API-base da avaliação de SW II. Complete os TODOs."""
import os
from datetime import timedelta

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        # Chave local de demonstração. Em produção, configure JWT_SECRET_KEY.
        JWT_SECRET_KEY=os.environ.get(
            "JWT_SECRET_KEY", "chave-didatica-local-sw-ii-nao-usar-em-producao"
        ),
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30),
    )
    if test_config:
        app.config.update(test_config)

    jwt = JWTManager(app)
    # Cada aplicação possui sua própria lista: os testes não compartilham dados.
    tarefas = [{"id": 1, "titulo": "Estudar Flask", "situacao": "pendente"}]
    usuarios = {
        "aluno": generate_password_hash("123456")
    }

    @jwt.unauthorized_loader
    def token_ausente(motivo):
        return jsonify({"erro": "Token de acesso ausente."}), 401

    @jwt.invalid_token_loader
    def token_invalido(motivo):
        return jsonify({"erro": "Token de acesso inválido."}), 401

    @jwt.expired_token_loader
    def token_expirado(header, payload):
        return jsonify({"erro": "Token de acesso expirado."}), 401

    @app.post("/login")
    def login():
        dados = request.get_json(silent=True)
        if not isinstance(dados, dict):
            return jsonify({"erro": "Envie um objeto JSON."}), 400

        usuario = dados.get("usuario")
        senha = dados.get("senha")
        if not isinstance(usuario, str) or not isinstance(senha, str):
            return jsonify({"erro": "Informe usuário e senha como texto."}), 400

        # TODO 1: buscar o hash em usuarios.get(usuario).
        # TODO 2: verificar a senha com check_password_hash(hash, senha).
        # Credenciais incorretas: retornar erro em JSON e status 401.
        # Credenciais corretas: criar token com create_access_token(identity=usuario).
        # Retornar {"access_token": token} e status 200.
        return jsonify({"erro": "Login ainda não implementado."}), 501

    @app.get("/tarefas")
    def listar_tarefas():
        # Exemplo pronto para consultar durante a implementação.
        return jsonify(tarefas), 200

    @app.post("/tarefas")
    # TODO 3: adicionar aqui o decorador @jwt_required().
    def cadastrar_tarefa():
        dados = request.get_json(silent=True)
        if not isinstance(dados, dict):
            return jsonify({"erro": "Envie um objeto JSON."}), 400

        # TODO 4: obter titulo, verificar se é texto e aplicar strip().
        # Se ausente, vazio ou composto só de espaços: retornar erro e status 400.
        # TODO 5: gerar um ID único (maior ID atual + 1).
        # Criar {"id": ..., "titulo": ..., "situacao": "pendente"}.
        # Adicionar à lista tarefas e retornar a tarefa com status 201.
        return jsonify({"erro": "Cadastro ainda não implementado."}), 501

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
