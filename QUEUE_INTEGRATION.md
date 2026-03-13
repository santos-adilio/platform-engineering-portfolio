# Integracao com ohio_queue - Ohio_MainBot

Documentacao da parte do `/redm/bots/Ohio_MainBot` relacionada a whitelist/IP usada pelo ohio_queue.

## Visao geral

O Ohio_MainBot fornece uma experiencia de Discord para o jogador gerar um link de conexao e registrar IPs. Ele tambem expõe uma API HTTP que grava e consulta IPs whitelisted em um banco SQLite local (`tickets.db`).

O ohio_queue consome uma API de whitelist definida em `ohio_queue/config.lua`. Para o fluxo completo funcionar, a origem de dados da API usada pelo ohio_queue deve refletir os IPs registrados por esse bot (diretamente ou por sincronizacao externa).

## Componentes principais

### Servidor de API (IP whitelist)

- Arquivo: `bots/Ohio_MainBot/ipwhitelist.js`
- Inicializacao: `setupApiServer()` chamado em `bots/Ohio_MainBot/bot.js`.
- Porta: `config.json -> ipWhitelist.apiPort` (padrao 3002).

Endpoints principais:

- `GET /api/ipwhitelist/health`
- `POST /api/ipwhitelist/validate-token`
- `POST /api/ipwhitelist/check-auth`
- `POST /api/ipwhitelist/save-ip`
- `GET /api/ipwhitelist/list`
- `POST /api/ipwhitelist/notify-complete`

### Fluxo de geracao de link (Discord)

- Arquivo: `bots/Ohio_MainBot/ipwhitelist.js`
- Botao: `ipwhitelist_connect_button`
- Processo:
  1) Usuario clica no botao.
  2) Bot gera token temporario (5 minutos) e salva em `whitelist_tokens`.
  3) Bot cria um link para o painel (`config.json -> ipWhitelist.panelUrl`) com query params de token e role.
  4) Usuario abre o painel para registrar IP.

### Banco local (SQLite)

- Arquivo: `bots/Ohio_MainBot/database.js`
- Banco: `bots/Ohio_MainBot/tickets.db`
- Tabelas relevantes:
  - `ip_whitelist` (discord_id, ip, created_at, expires_at)
  - `whitelist_tokens` (token, discord_id, created_at, expires_at)
  - `rotation_auth_tokens` (token_hash, created_at, expires_at)

## Autenticacao da API

O bot usa um token rotativo baseado em `config.json -> ipWhitelist.rotationSecret`.

- `generateRotationToken()` cria token por hora.
- `validateRotationToken()` aceita hora atual ou anterior com tolerancia de 5 minutos.

Esse token e exigido nos endpoints sensiveis (`check-auth`, `save-ip`, `list`).

## Relacao com ohio_queue

- `ohio_queue` valida o jogador via `Config.API.BASE_URL`.
- O bot registra IPs via painel e grava em SQLite.
- Para a validacao funcionar, a API usada pelo ohio_queue deve acessar a mesma fonte de IPs (ou uma replica sincronizada).

## Diagrama de integracao

```
Discord User
  -> Ohio_MainBot (ipwhitelist.js)
  -> gera token e link de painel
  -> painel registra IP via API do bot
  -> IP salvo em tickets.db (ip_whitelist)

ohio_queue
  -> chama API de whitelist (Config.API.BASE_URL)
  -> autoriza ou bloqueia conexao
```

