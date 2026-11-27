# Segurança — ODIN FORCE

## Estado atual (v0.1)

Implementado:
- Configuração por variáveis de ambiente; `.env` ignorado pelo Git.
- Documentação interativa da API desativada fora do modo debug.
- Resposta do health check sem dados sensíveis.

**Não implementado:** autenticação, controle de permissões, auditoria de
execução, isolamento de workspace, cofre de credenciais. Até existirem, a
aplicação deve rodar apenas em `127.0.0.1`.

## Regras do projeto

1. Nenhum segredo no repositório. Use `.env` local (fora do Git).
2. Chaves de API nunca vão ao frontend nem aos logs.
3. Toda ferramenta futura terá: schema de entrada validado, permissão própria,
   log de execução e aprovação humana para ações sensíveis.
4. Comandos de terminal: allowlist, timeout e diretório restrito ao workspace.
   Operações destrutivas exigem confirmação explícita.
5. Workspaces: verificação de caminho (anti path traversal). Em Termux isso
   **não é** um sandbox real; é uma proteção contra acidentes.
6. Funcionalidades de cibersegurança operam somente em laboratórios próprios ou
   alvos com autorização e escopo documentados. O escopo será verificado em
   código (lista de alvos permitidos), não apenas por convenção.
7. Fora de escopo, por decisão de projeto: roubo de credenciais, acesso não
   autorizado, furtividade e funcionalidades destrutivas.

## Reportar problemas

Projeto privado: registre como issue privada ou avise o proprietário.
