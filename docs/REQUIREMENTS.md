# REQUIREMENTS.md  

## 1. Overview  
**Project Name:** itinerary-guard  
**Product Type:** Real‑time travel‑info verification service  
**Goal:** Cross‑check user‑provided travel itineraries against multiple authoritative data sources (airlines, rail operators, hotels, car‑rental agencies, and government travel advisories) and flag any inconsistencies **before** a booking is confirmed.  

The service must operate with low latency, high availability, and strong data security to support integration into booking platforms, travel agencies, and corporate travel tools.

---

## 2. Functional Requirements  

| ID | Description |
|----|-------------|
| **FR‑1** | **Input API** – Expose a RESTful `POST /verify` endpoint that accepts a JSON payload containing a full itinerary (flights, trains, hotels, car rentals, passenger details, dates, times, and booking references). |
| **FR‑2** | **Source Connectors** – Implement adapters for at least the following authoritative sources (configurable via plugin): <br>• Airline PNR APIs (e.g., SITA, Amadeus) <br>• Rail operator APIs (e.g., Eurail, Amtrak) <br>• Hotel reservation systems (e.g., Booking.com, Expedia) <br>• Car‑rental APIs (e.g., Hertz, Avis) <br>• Government travel advisory feeds (e.g., US DOT, EU REACH) |
| **FR‑3** | **Data Normalisation** – Convert all source responses into a canonical itinerary model (flight segment, rail segment, hotel stay, car rental) with unified fields (carrier, departure/arrival timestamps, location codes, booking reference). |
| **FR‑4** | **Verification Logic** – For each itinerary element, cross‑check the user‑provided data against the authoritative source(s) and produce a verification status: `VALID`, `MISMATCH`, `NOT_FOUND`, or `ERROR`. |
| **FR‑5** | **Inconsistency Reporting** – Return a structured response listing each element with its verification status, a human‑readable message, and a confidence score (0‑100%). |
| **FR‑6** | **Batch Processing** – Support verification of up to **500** itinerary elements in a single request without degrading latency beyond the limits defined in NFR‑1. |
| **FR‑7** | **Webhook Callback** – Optionally accept a `callback_url` in the request; upon completion, POST the verification result to the supplied URL. |
| **FR‑8** | **Audit Log** – Persist every verification request and result (including raw source responses) to an immutable audit store for 90 days, searchable by request ID, user ID, and timestamp. |
| **FR‑9** | **Rate Limiting** – Enforce per‑client quotas (default 100 requests/minute) and return HTTP 429 when exceeded. |
| **FR‑10** | **Admin Dashboard** – Provide a minimal UI for ops to view recent verification jobs, error rates, and health of source connectors. |
| **FR‑11** | **Feature Flags** – All source connectors must be toggleable at runtime via a configuration service (e.g., LaunchDarkly‑compatible). |
| **FR‑12** | **Internationalisation** – Accept and return dates/times in ISO‑8601 and support localisation of error messages for at least English, Spanish, and Mandarin. |

---

## 3. Non‑Functional Requirements  

| ID | Requirement |
|----|-------------|
| **NFR‑1** | **Performance** – 95 % of `POST /verify` calls must complete within **300 ms** (including external source calls) under normal load (≤ 200 RPS). 99 % latency ≤ 600 ms. |
| **NFR‑2** | **Scalability** – System must be horizontally scalable; add new instances to handle up to **5 k RPS** with linear throughput. |
| **NFR‑3** | **Reliability** – Achieve **99.9 %** uptime (excluding scheduled maintenance). Automatic failover for any source connector that becomes unavailable. |
| **NFR‑4** | **Security** – All inbound/outbound traffic must use TLS 1.3. Data at rest encrypted with AES‑256. JWT‑based authentication for API clients; scopes: `verify:itinerary`. |
| **NFR‑5** | **Privacy** – Do not store personally identifiable information (PII) longer than required for audit (max 90 days). Provide data‑deletion endpoint for GDPR compliance. |
| **NFR‑6** | **Observability** – Emit structured logs, Prometheus metrics (request latency, error rates, source‑connector health), and OpenTelemetry traces for end‑to‑end request flow. |
| **NFR‑7** | **Compliance** – Meet PCI‑DSS (if payment data ever passes through) and ISO 27001 baseline controls. |
| **NFR‑8** | **Maintainability** – Codebase must follow the Axentx C++/Python style guide, include unit test coverage ≥ 85 % and integration test coverage ≥ 70 %. |
| **NFR‑9** | **Deployment** – Containerised (Docker) with Helm charts for Kubernetes (v1.27+). Must support blue‑green deployments with zero‑downtime switch. |
| **NFR‑10** | **Extensibility** – New source connectors must be implementable as plug‑ins adhering to the `IConnector` interface without core code changes. |
| **NFR‑11** | **Resource Usage** – Each service instance must not exceed **2 CPU** and **4 GiB RAM** under peak load. |
| **NFR‑12** | **Testing** – Include contract tests (Pact) for each external API integration. |

---

## 4. Constraints  

1. **Technology Stack** – Must use the verified Axentx frameworks:  
   * **vLLM** for any LLM‑based fuzzy matching of free‑text fields.  
   * **SGLang** for structured generation of verification messages.  

2. **Data Sources** – Only use publicly documented APIs or data feeds that permit commercial use under existing licences (Apache‑2.0, MIT, CDLA‑Permissive‑2.0).  

3. **Latency** – External API calls must be parallelised; total external‑call time cannot dominate the 300 ms SLA.  

4. **Repository Size** – The final binary must stay under **150 MiB** to fit within Axentx CI artifact limits.  

5. **Compliance** – No third‑party library with a GPL license may be included.  

6. **Versioning** – Follow Semantic Versioning 2.0.0; initial release will be `1.0.0`.  

---

## 5. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | Authoritative source APIs provide near‑real‑time data (≤ 2 s freshness). |
| **A‑2** | Clients will provide itineraries in the canonical JSON schema defined in `schema/itinerary.json`. |
| **A‑3** | Network connectivity between Axentx data centre and external sources is reliable (≤ 50 ms RTT). |
| **A‑4** | The audit store (e.g., ClickHouse) is provisioned and accessible via the internal service mesh. |
| **A‑5** | Rate‑limit quotas can be overridden per‑client via the admin dashboard. |
| **A‑6** | All localisation strings are stored in the existing Axentx i18n repository and can be imported at build time. |
| **A‑7** | The product will initially launch in North America and Europe; source connectors for other regions are out of scope for MVP. |
| **A‑8** | The JWT signing keys are managed by the Axentx secret‑management service and rotated quarterly. |

---

## 6. Acceptance Criteria  

1. **Functional** – All FR‑1 – FR‑12 are demonstrably working in an end‑to‑end integration test against at least three live source APIs.  
2. **Performance** – Load test (k6) shows 95 % of requests ≤ 300 ms at 200 RPS.  
3. **Security** – Pen‑test report (OWASP Top 10) passes with no critical findings.  
4. **Reliability** – Chaos‑mesh experiments confirm automatic failover of a source connector without request failure.  
5. **Documentation** – API spec (OpenAPI 3.1), deployment guide, and operational runbook are committed to the repo.  

---  

*Prepared by the Senior Product/Engineering Lead, Axentx – 2026‑06‑19*
