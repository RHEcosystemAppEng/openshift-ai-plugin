# Red Hat Connectivity Link (RHCL)

Kuadrant-based **Gateway API ingress control plane** on OpenShift: attaches `TLSPolicy`, `AuthPolicy`, `RateLimitPolicy`, and `DNSPolicy` to `Gateway` / `HTTPRoute` so teams secure, rate-limit, and (with DNS) multicluster-balance north-south traffic without embedding networking in apps. Peers are DIY Istio/Envoy gateway stacks, Kong/NGINX/other API connectivity layers, and upstream Kuadrant without Red Hat packaging—what teams run instead of (or before) adopting **RHCL** as the policy plane under inference/MCP gateways.

## Peers

- Kuadrant upstream (community) — Authorino / Limitador / DNS Operator + `AuthPolicy`/`RateLimitPolicy`/`TLSPolicy`/`DNSPolicy` without `rhcl-operator` / Connectivity Link packaging
- DIY Istio / Envoy Gateway API gateways — Gateway API (or Istio Gateway) + hand-rolled EnvoyFilter / wasm / ext_authz / global rate-limit for auth, TLS, and limits on north-south AI routes
- OpenShift Service Mesh gateway DIY — OSSM/Istio as the Gateway API provider with mesh AuthorizationPolicy / RequestAuthentication / EnvoyFilter instead of Kuadrant CRs
- Kong Gateway / Kong Ingress Controller — Kong/Konnect plugins (OIDC, rate-limiting, JWT, AI Proxy) as the API connectivity layer in front of inference or MCP backends
- NGINX Ingress alone — Ingress annotations/`nginx.ingress.kubernetes.io/*` for TLS, auth, and rate limits on AI/MCP routes (no Gateway API + Kuadrant policy plane)
- Envoy Gateway / Envoy AI Gateway (standalone) — community Envoy Gateway or `envoyproxy/ai-gateway` with native SecurityPolicy / BackendTrafficPolicy / AI routes instead of RHCL
- Solo Gloo / Gloo Gateway — Gloo Gateway API + AuthConfig / RateLimitConfig (or Gloo AI Gateway) as the connectivity/policy plane
- Traefik / Contour / HAProxy Ingress — Traefik Middleware, Contour HTTPProxy, or HAProxy Ingress CRDs for L7 auth/rate-limit/TLS on model or agent routes
- Apache APISIX / Tyk / other OSS API gateways — APISIX/Tyk (or similar) plugins for JWT, rate limit, and upstream routing to LLM/MCP Services
- Apigee / enterprise API management — Apigee (or similar) as the north-south connectivity and policy layer for AI APIs
- oauth2-proxy + DIY rate-limit sidecars — oauth2-proxy / Keycloak gatekeeper + Redis/nginx limit_req in front of inference/MCP without Gateway API policies
- Plain OpenShift Route / Ingress / HTTPRoute — single-cluster exposure with no AuthPolicy/RateLimitPolicy/TLSPolicy/DNSPolicy control plane

**Not peers (adjacent catalog jobs):** MCP Gateway / MCP Gateway Authorization (TP features *on* RHCL, not substitutes for the platform); Gateway API Inference Extensions / llm-d (inference scheduling that *uses* a gateway—often RHCL—not the connectivity policy plane itself); OpenShift Service Mesh east-west mTLS/sidecars as a whole-mesh substitute (complementary data plane, not RHCL’s north-south policy job).

## Detection aliases

- Kuadrant upstream: `kuadrant.io`, community `kuadrant-operator` / Authorino / Limitador Helm or OLM **without** `rhcl-operator` / `redhat-operators` Connectivity Link Subscription; `Kuadrant` CR in non-RH installs
- DIY Istio/Envoy gateways: EnvoyFilter/`ext_authz`/`ratelimit` on Gateway; wasm auth filters; hand-rolled Envoy GatewayClass for AI ingress; “DIY Gateway API policy” ADRs
- OSSM gateway DIY: Service Mesh as sole Gateway API provider + `AuthorizationPolicy`/`RequestAuthentication`/`EnvoyFilter` on ingress Gateway (no `AuthPolicy`/`RateLimitPolicy` Kuadrant CRs)
- Kong: Kong Ingress Controller / Kong Gateway / Konnect; `konghq.com` Ingress/Gateway plugins; `ai-proxy` / rate-limiting / OIDC plugins in front of LLM or MCP Services
- NGINX Ingress alone: `ingress-nginx`, `nginx.ingress.kubernetes.io/auth-*`, `limit-rps`/`limit-connections`, TLS annotations on AI/MCP Ingress (no `Gateway`+Kuadrant)
- Envoy Gateway / Envoy AI Gateway: `envoyproxy/gateway`, `envoyproxy/ai-gateway`, Envoy Gateway `SecurityPolicy`/`BackendTrafficPolicy` without RHCL
- Solo Gloo: Gloo Gateway / Gloo Edge `AuthConfig`/`RateLimitConfig`; Solo AI Gateway as connectivity layer
- Traefik / Contour / HAProxy: Traefik `Middleware` ForwardAuth/rateLimit; Contour `HTTPProxy`; HAProxy Ingress CRDs for model routes
- APISIX / Tyk: `apache/apisix`, Tyk Gateway plugins for JWT/rate-limit to LLM/MCP upstreams
- Apigee / enterprise APIM: Apigee AI/LLM proxy or enterprise API gateway as north-south front door
- oauth2-proxy DIY: `oauth2-proxy`, Keycloak gatekeeper, nginx `limit_req` / Redis rate-limit sidecars in front of inference/MCP Deployments
- Plain Route/Ingress/HTTPRoute: OpenShift `Route` / `Ingress` / bare `HTTPRoute`→Service with **no** `TLSPolicy`/`AuthPolicy`/`RateLimitPolicy`/`DNSPolicy`

## Row (for table)

| Kuadrant upstream (no RH packaging); DIY Istio/Envoy Gateway API + EnvoyFilter/ext_authz/rate-limit; OSSM gateway AuthorizationPolicy DIY; Kong Gateway/KIC; NGINX Ingress alone for AI routes; Envoy Gateway / Envoy AI Gateway; Solo Gloo Gateway; Traefik/Contour/HAProxy Ingress; Apache APISIX/Tyk; Apigee/enterprise APIM; oauth2-proxy + DIY rate-limit; plain Route/Ingress/HTTPRoute | Red Hat Connectivity Link (RHCL) | kuadrant-operator/Authorino/Limitador without rhcl-operator; EnvoyFilter ext_authz/ratelimit on Gateway; OSSM AuthorizationPolicy/RequestAuthentication on ingress; Kong/KIC/Konnect AI/OIDC/rate-limit plugins; ingress-nginx auth-/limit-* annotations; envoyproxy/gateway / envoyproxy/ai-gateway SecurityPolicy; Gloo AuthConfig/RateLimitConfig; Traefik Middleware / Contour HTTPProxy / HAProxy Ingress; apisix/tyk JWT+rate-limit; Apigee AI front door; oauth2-proxy + nginx/Redis limits; Route/Ingress/HTTPRoute with no Kuadrant policies |
