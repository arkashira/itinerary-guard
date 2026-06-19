# 🚀 Itinerary‑Guard Roadmap  

*Version: 1.0 – Updated 2026‑06‑19*  

---  

## 📖 Overview  

**Itinerary‑Guard** is a real‑time travel‑information verification service that cross‑checks user‑submitted itineraries against multiple authoritative sources (airlines, GDS, OTA, rail operators, etc.) and flags inconsistencies **before** a booking is finalized.  

The roadmap is organized around three delivery horizons:  

| Horizon | Codename | Goal | Target Release |
|---------|----------|------|----------------|
| **MVP** | **Launch‑Ready** | Core verification flow, API, and monitoring – **must‑have for launch** | **Q3 2026** |
| **v1** | **Expansion** | Broader transport coverage, AI‑assisted anomaly detection, integrations | **Q4 2026** |
| **v2** | **Intelligence** | Predictive risk scoring, auto‑correction, marketplace & mobile SDK | **Q2 2027** |

> **MVP‑critical** items are highlighted with a 🔴 badge.  

---  

## 🎯 MVP – Launch‑Ready (🔴 Critical)

| # | Feature | Description | Acceptance Criteria |
|---|---------|-------------|----------------------|
| 1️⃣ | **Itinerary Ingestion API** | REST endpoint (`POST /v1/itineraries`) that accepts JSON payloads for flights, hotels, and car rentals. | - Returns `202 Accepted` with a unique `verification_id`.<br>- Validates schema (OpenAPI v3). |
| 2️⃣ | **Source Connectors (Flight & Hotel)** | Pull authoritative data from: <br>• Airline APIs (e.g., Amadeus, Sabre) <br>• Hotel OTA APIs (Booking.com, Expedia). | - ≥ 95 % success rate on live test itineraries.<br>- Handles OAuth2 & API‑key auth. |
| 3️⃣ | **Cross‑Check Engine** | Compare each itinerary leg with source data (times, airports, reservation codes). | - Flags any mismatch with severity levels (Info/Warning/Error). |
| 4️⃣ | **Result API & Dashboard** | `GET /v1/verification/{id}` returns verification report; simple web UI for internal ops to view flagged items. | - UI shows summary, detailed diff, and export to CSV. |
| 5️⃣ | **Rate Limiting & Quotas** | Protect external APIs and internal services (token bucket per client). | - 100 req/s global limit, 10 req/s per API key. |
| 6️⃣ | **Observability** | Structured logging, Prometheus metrics, Grafana dashboards, and alerting on error spikes. | - SLA ≥ 99.5 % for verification latency ≤ 2 s. |
| 7️⃣ | **Security & Compliance** | TLS everywhere, API‑key auth, GDPR‑compliant data retention (30 days). | - Pass internal security audit. |
| 8️⃣ | **CI/CD Pipeline** | Automated tests, Docker image build, Helm chart for K8s deployment. | - 80 %+ test coverage, zero‑downtime rollout. |

**MVP Success Metric:** Process **≥ 10 k** itineraries in the first month with **< 1 %** false‑negative rate (i.e., missed inconsistencies).

---  

## 🌱 v1 – Expansion (Q4 2026)

| Theme | Feature | Shippable Scope |
|-------|---------|-----------------|
| **Broader Transport** | Add **Rail**, **Cruise**, and **Inter‑city Bus** connectors (e.g., Rail Europe, CruiseLine APIs). | Unified connector interface; 80 % coverage of EU rail operators. |
| **AI‑Assisted Anomaly Detection** | Deploy **vLLM** inference engine to run a lightweight LLM that suggests probable causes for mismatches (e.g., schedule change, code‑share). | Model served via SGLang for structured output; latency ≤ 500 ms per itinerary. |
| **Batch Verification** | Endpoint `POST /v1/itineraries/batch` for bulk uploads (CSV/JSON). | Process up to 5 k itineraries per request, async result polling. |
| **Webhook Integration** | Allow partners to receive real‑time verification results via configurable webhooks. | Retry logic, signature verification, delivery SLA ≤ 1 s. |
| **Audit Trail & Versioning** | Immutable log of every verification request & source snapshot (stored in PostgreSQL + S3). | Ability to retrieve historic verification for compliance. |
| **SLA & Reliability Enhancements** | Auto‑scale based on queue depth, circuit‑breaker for flaky external APIs. | 99.9 % uptime SLA for core services. |
| **Documentation Portal** | Swagger UI + developer portal with SDKs (Python, Node). | SDKs published to PyPI & npm. |

**v1 Success Metric:** Support **≥ 3 transport modes** and achieve **≤ 200 ms** average L
