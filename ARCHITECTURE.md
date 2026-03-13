# Arquitetura - ohio_queue

Documentacao da arquitetura do resource `/redm/ohio_queue`, com foco em componentes, fluxo de verificacao e integracoes.

## Visao geral

O ohio_queue e um sistema de fila para RedM que valida o jogador via API externa antes de permitir a conexao. A validacao e baseada em IP e Discord ID (obrigatorios), com Steam ID opcional.

## Componentes principais

### Manifest

- Arquivo: `ohio_queue/fxmanifest.lua`
- Registra scripts cliente/servidor do resource.

### Configuracao

- Arquivo: `ohio_queue/config.lua`
- Define:
  - API de whitelist (URL base e token).
  - Regras obrigatorias (IP/Discord/Steam).
  - Pontuacao da fila (ganho e perda).
  - Mensagens de erro.
  - VIPs e roles com prioridade.
  - Bypass de emergencia.

### Servidor (fila e validacao)

- Arquivo: `ohio_queue/server.lua`
- Responsavel por:
  - Controlar a fila e a pontuacao por tempo.
  - Buscar identificadores (discord, steam, ip, license).
  - Validar via API externa:
    - IP na whitelist.
    - Discord com IPs cadastrados.
    - IP atual vinculado ao Discord.
  - Logar eventos de seguranca (fail2ban).
  - Exibir mensagens de erro e controlar entrada.

### Cliente

- Arquivo: `ohio_queue/client.lua`
- Envia evento para o servidor quando o jogador termina de carregar.

## Integracao com API de whitelist

Fonte configurada em `ohio_queue/config.lua`:

- Base URL: `Config.API.BASE_URL`
- Token: `Config.API.TOKEN`

Endpoints usados no servidor:

- `GET /api/whitelist/check/:ip`
- `GET /api/whitelist/user/:discordId`

A API precisa retornar dados consistentes com a whitelist que o servidor usa. O resource depende desse resultado para permitir a conexao.

## Fluxo de conexao (alto nivel)

```
Jogador conecta
  -> identificar discord/steam/ip
  -> valida IP na whitelist (API)
  -> valida Discord com IPs (API)
  -> valida IP vinculado ao Discord (API)
  -> entra na fila e aguarda vaga
  -> autorizado a conectar
```

## Seguranca e observabilidade

- Log de eventos para fail2ban em `/redm/f2blogs.log`.
- Rate de tentativas por IP com janela e limite (detecao de bruteforce).
- Mensagens customizadas para erros comuns de validacao.

## Diagrama de componentes

```
RedM Client -> ohio_queue (client.lua)
                 |
                 v
           ohio_queue (server.lua)
                 |
                 v
      API Whitelist (Config.API.BASE_URL)
```

