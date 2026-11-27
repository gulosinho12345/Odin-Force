# Arquitetura — ODIN FORCE v0.1

## Princípio

Monólito modular: um único processo FastAPI, módulos separados por pacote.
Sem microsserviços, sem filas, sem Docker (não disponível no Termux).

## Estrutura

```
odin-force/
├── backend/
│   ├── app/
│   │   ├── main.py            # create_app(): monta a aplicação
│   │   ├── config.py          # Settings (ODIN_*)
│   │   ├── logging_config.py  # logs JSON (stdlib)
│   │   ├── api/               # rotas HTTP (implementado: health)
│   │   ├── core/              # [reservado] Core Engine
│   │   ├── providers/         # [reservado] Provider System / Model Manager
│   │   ├── tools/             # [reservado] Tool Engine
│   │   ├── memory/            # [reservado] Project Memory
│   │   └── security/          # [reservado] Permissões, auditoria, escopo
│   └── tests/
├── docs/
├── workspaces/                # área de trabalho dos projetos (ignorada pelo Git)
├── requirements.txt / requirements-dev.txt
├── pytest.ini
└── .env.example
```

Módulos futuros mapeados para pacotes:

| Módulo do brief | Onde vai viver |
|---|---|
| Core Engine | `app/core/` |
| Model Manager + Provider System | `app/providers/` |
| Development Engine | `app/core/` (agente) usando `app/tools/` |
| Cybersecurity Engine | `app/tools/` (ferramentas) + `app/security/` (escopo) |
| Tool Engine | `app/tools/` |
| Project Memory | `app/memory/` |
| Security & Permissions | `app/security/` |
| API Layer | `app/api/` |
| User Interface | `frontend/` (a criar) |

Os pacotes só ganham código quando a task correspondente começar. Nada de
classes base especulativas agora.

## Decisões

1. **`create_app()` em vez de app global puro** — permite testes com
   configuração isolada.
2. **Dependências mínimas** (`fastapi`, `uvicorn`, `pydantic-settings`).
   Sem `uvicorn[standard]` (uvloop/httptools exigem compilação no Termux).
   `httpx` e `pytest` só em `requirements-dev.txt`.
3. **Logs JSON via stdlib** — evita dependência (`structlog`) por ora.
4. **`/docs` e `/openapi.json` só com `ODIN_DEBUG=true`** — menos superfície.
5. **Bind em `127.0.0.1`** por padrão nos comandos documentados. A API ainda
   não tem autenticação; não exponha na rede.
6. **Provedores (futuro)** — interface única (`chat(messages, params)`) com um
   adaptador OpenAI-compatível primeiro (cobre OpenAI, OpenRouter, Groq),
   depois Anthropic e Gemini. Chaves só via ambiente, nunca no frontend.
7. **Frontend (futuro)** — HTML/CSS/JS estáticos servidos pelo FastAPI
   primeiro; React/TypeScript só se houver necessidade real.
8. **Banco (futuro)** — SQLite. Nenhuma dependência de banco no v0.1.

## Compatibilidade

- Python 3.10+ (Termux atual traz 3.12 ou superior).
- `pydantic-core` pode precisar de compilação (Rust) no Termux. Não testado
  em dispositivo real neste momento.
