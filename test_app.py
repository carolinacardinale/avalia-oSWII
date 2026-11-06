"""Complete os testes. Os testes pendentes devem falhar até serem escritos."""
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def auth_headers(client):
    resposta = client.post(
        "/login", json={"usuario": "aluno", "senha": "123456"}
    )
    assert resposta.status_code == 200
    token = resposta.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_consulta_tarefas(client):
    # Teste de exemplo já implementado.
    resposta = client.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.get_json(), list)
    assert resposta.get_json()[0]["titulo"] == "Estudar Flask"


def test_login_correto(client):
    # POST /login: verificar status 200 e token como texto não vazio.
    pytest.fail("TODO: implementar teste de login correto")


def test_login_senha_incorreta(client):
    # Verificar status 401 e ausência de access_token.
    pytest.fail("TODO: implementar teste de senha incorreta")


def test_cadastro_sem_token(client):
    # Enviar um título válido sem Authorization.
    # Verificar status 401 e que a lista permaneceu igual.
    pytest.fail("TODO: implementar teste de cadastro sem token")


def test_cadastro_com_token(client, auth_headers):
    # Usar client.post(..., json={...}, headers=auth_headers).
    # Verificar 201, título, situação e ID diferente dos existentes.
    # Consultar GET /tarefas e confirmar que a nova tarefa foi persistida.
    pytest.fail("TODO: implementar teste de cadastro autenticado")


@pytest.mark.parametrize("dados", [{}, {"titulo": ""}, {"titulo": "   "}])
def test_cadastro_titulo_vazio(client, auth_headers, dados):
    # Enviar cada caso com token válido; verificar 400 e lista inalterada.
    pytest.fail("TODO: implementar teste de título ausente ou vazio")
