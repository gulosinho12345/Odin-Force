# ODIN FORCE

Plataforma modular de agentes de IA multi-modelo. **Status: v0.1 — apenas a fundação.**

## O que existe hoje

- Aplicação FastAPI mínima com `GET /api/v1/health`
- Configuração por variáveis de ambiente, logs JSON, testes com pytest

## O que NÃO existe ainda

Core Engine, Model Manager, provedores de IA, ferramentas, memória, módulo de
cibersegurança e interface web. Os diretórios correspondentes em `backend/app/`
são apenas reservas de nome (ver `docs/ARCHITECTURE.md`).

## Instalação (Termux)

```bash
pkg update && pkg upgrade -y
pkg install -y python git
git clone <URL-DO-SEU-REPOSITORIO-PRIVADO> odin-force
cd odin-force
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cp .env.example .env
```

Se o `pip install` falhar compilando `pydantic-core` (Rust), rode
`pkg install -y rust binutils` e tente de novo.

## Executar

```bash
uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000
```

Em outra sessão do Termux:

```bash
curl http://127.0.0.1:8000/api/v1/health
```

Saída esperada:

```json
{"status":"ok","app":"ODIN FORCE","version":"0.1.0","environment":"development"}
```

## Testes

```bash
pytest
```

Esperado: `4 passed`.

## Configuração

Veja `.env.example`. Nunca faça commit do `.env`.
