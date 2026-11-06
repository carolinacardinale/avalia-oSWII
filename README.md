# Avaliação prática — SW II

## Desafio
Complete a API de tarefas e os testes em quatro aulas de 50 minutos, em dupla.
O projeto é uma base intencionalmente incompleta: os TODOs são parte da avaliação.

## Preparação (Windows / PowerShell)
Abra esta pasta no VS Code e execute no terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

A API ficará em http://127.0.0.1:5000. Mantenha esse terminal aberto para usar
Bruno/Postman. Para parar, pressione Ctrl+C. Não é necessário ativar o ambiente.

Em Linux/macOS, use `python3 -m venv .venv` e substitua o executável dos
comandos seguintes por `.venv/bin/python`.

## Executar os testes
Em outro terminal, na mesma pasta:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Os testes criam sua própria aplicação: não precisam do servidor aberto.
Inicialmente, há um teste pronto e sete casos pendentes que falham
intencionalmente (o teste de título executa três exemplos).
Não apague os testes pendentes: substitua cada `pytest.fail(...)` pela sua
implementação e pelas verificações solicitadas nos comentários.

## Credenciais de demonstração
- Usuário: `aluno`
- Senha: `123456`

A senha já é armazenada como hash. Não compare a senha digitada diretamente
com o hash: utilize `check_password_hash`.

## Roteiro
1. Aula 1: executar a base e completar a validação do login e geração do JWT.
2. Aula 2: proteger POST /tarefas e implementar validação e cadastro.
3. Aula 3: completar os testes, executar o Pytest e corrigir os erros.
4. Aula 4: finalizar este README e demonstrar a API à professora.

## Contrato da API
| Método | Rota | Resultado esperado |
| --- | --- | --- |
| POST | /login | 200 e access_token, ou 401 para credenciais incorretas |
| GET | /tarefas | 200 e lista de tarefas |
| POST | /tarefas | 201 e tarefa criada; exige JWT |

POST /login — corpo JSON:
```json
{"usuario": "aluno", "senha": "123456"}
```

POST /tarefas — corpo JSON:
```json
{"titulo": "Revisar os testes da API"}
```

No Bruno/Postman, selecione corpo JSON e utilize Content-Type: application/json.
Para cadastrar, adicione o cabeçalho `Authorization: Bearer SEU_TOKEN`.
Título ausente, vazio ou só com espaços: 400. Sem token: 401.
O identificador deve ser único e a situação inicial deve ser `pendente`.

## O que já está pronto
Configuração do Flask/JWT, hash do usuário, dados iniciais, consulta de tarefas,
tratamento de erros do JWT, fixtures e um teste de consulta.
As rotas incompletas retornam 501 até serem implementadas.

## Limites deste projeto didático
Dados em memória são perdidos ao reiniciar. As tarefas são compartilhadas entre
os usuários autenticados; não há separação por proprietário.
Credenciais e chave local são apenas para demonstração. Não publicar esta base
como serviço de produção. O modo debug é destinado à execução local.

