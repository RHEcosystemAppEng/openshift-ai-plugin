# MCP Authorization Server

Red Hat build of Keycloak as an OAuth 2.0/2.1 **authorization server** for MCP hosts and resource servers—token issuance, DCR, and (experimental) CIMD—so clients get audience-bound access without embedding IdP logic in each MCP server. Peers are DIY API-key / embedded-auth patterns and other IdPs used as MCP AS (often without CIMD / MCP-scoped setup) that teams adopt instead of the catalog **MCP Authorization Server** path.

## Peers

- DIY API keys in IDE `mcp.json` / `mcpServers` — long-lived tokens or static keys hard-coded in Cursor / Claude / VS Code for remote HTTP MCP (no external AS)
- Embedded login / token minting in the MCP process — hand-rolled OAuth AS inside each server (login UI, consent, client store, JWT mint) instead of an external IdP
- Custom “auth microservice” for MCP JWTs — thin token issuer without full OIDC (no RFC 8414 metadata, PKCE, DCR/CIMD)
- Upstream / community Keycloak as MCP AS (non-RH) — Keycloak MCP guide / Operator outside Red Hat build; migrate *into* RH build of Keycloak catalog path
- Plain Keycloak / RHBK as generic IdP without MCP AS setup — OIDC for apps/console only; no PRM `authorization_servers`, `mcp:*` scopes, Audience-to-MCP-URL mappers, or CIMD
- Auth0 / Okta / Entra / WorkOS AuthKit as MCP AS — same *role* (enterprise OAuth for MCP hosts) without RH Keycloak CIMD / Audience-mapper MCP guide
- Community Keycloak+MCP templates — `mcp-use/mcp-oauth-keycloak-template`, `wadahiro/go-mcp-server-example`, Phase Two / Christian Posta tutorials (DIY AS wiring)
- Static client registration only — pre-registered OAuth clients for MCP hosts with no DCR and no CIMD (`client-id-metadata-document` / URL-form `client_id`)

**Not peers (adjacent catalog jobs):** MCP Gateway Authorization (tool/prompt CEL/OPA on gateway—not token issuance); MCP Gateway (federation); MCP Catalog / lifecycle (browse/deploy servers); Lightspeed OpenShift TokenReview for `/v1/query`; JWT *validation* alone on MCP servers/gateway (resource-server side—issuer is still the AS peer).

## Detection aliases

- DIY API keys: Cursor/Claude/VS Code `mcp.json` / `mcpServers` with `Authorization` / API key / long-lived bearer; comments “no IdP”, “static MCP token”
- Embedded AS: login/consent UI inside MCP server; in-process token minting; per-server client store; “MCP server as its own OAuth AS”
- Thin JWT issuer: custom auth microservice minting MCP JWTs without `/.well-known/oauth-authorization-server` / OIDC discovery / PKCE / DCR
- Upstream Keycloak MCP: keycloak.org `mcp-authz-server` guide; non-RH Keycloak Operator/`Keycloak` CR used as MCP AS; `--features=cimd` without `rhbk-operator`
- Plain Keycloak IdP: realm OIDC for OpenShift/apps only; missing PRM `authorization_servers`, `mcp:tools`/`mcp:prompts`/`mcp:resources`, Audience mapper to MCP URL, CIMD policy
- Auth0/Okta/Entra/WorkOS: Auth0 / Okta / Entra ID / WorkOS AuthKit as MCP authorization server / CIMD-or-DCR IdP (non-RH)
- Templates/tutorials: `mcp-use/mcp-oauth-keycloak-template`, `wadahiro/go-mcp-server-example`, Phase Two Keycloak MCP, Christian Posta MCP auth series
- Static clients: pre-registered MCP host clients only; no DCR `registration_endpoint`; no CIMD `client-id-metadata-document` / `client-id-uri` / URL-form `client_id`
- Protocol need-for-AS: RFC 9728 PRM; `WWW-Authenticate` `resource_metadata=`; auth code+PKCE; DCR/CIMD; “delegate auth to Keycloak”, “enterprise IdP for MCP hosts”

## Row for `MCP Authorization Server`

| DIY API keys in mcp.json/mcpServers; embedded MCP-process login/token minting; thin custom JWT auth microservice; upstream/community Keycloak MCP AS (non-RH); plain Keycloak/RHBK IdP without MCP scopes/CIMD/Audience mappers; Auth0/Okta/Entra/WorkOS as MCP AS; community Keycloak+MCP templates; static OAuth clients without DCR/CIMD | MCP Authorization Server | mcp.json / mcpServers API keys / static bearer; embedded MCP OAuth AS / in-process token mint; custom MCP JWT issuer without OIDC metadata; keycloak.org mcp-authz-server (non-RH); Keycloak without mcp:* scopes / CIMD / Audience mapper; Auth0 / Okta / Entra / WorkOS AuthKit MCP AS; mcp-use/mcp-oauth-keycloak-template; wadahiro/go-mcp-server-example; static MCP clients no DCR/CIMD; RFC 9728 PRM / resource_metadata / PKCE need-for-AS |
