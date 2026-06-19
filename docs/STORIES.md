# STORIES.md
**Project:** itinerary-guard  
**Product Vision:** A real‑time travel‑info verification service that cross‑checks user‑submitted itineraries against multiple authoritative sources (airlines, rail operators, hotels, visa databases, etc.) and flags inconsistencies before booking, reducing costly errors and improving traveler confidence.  

---  

## Epic 1 – Core Verification Engine (MVP)

| # | User Story |
|---|------------|
| **1.1** | **As a traveler, I want the system to instantly validate my flight segment against the airline’s official schedule, so that I know my flight details are correct before I book.** |
| **1.2** | **As a traveler, I want the system to cross‑check my hotel reservation dates with the hotel’s availability API, so that I avoid double‑booking or out‑of‑date stays.** |
| **1.3** | **As a traveler, I want the service to compare my visa requirements with the destination country’s entry rules, so that I can see if additional documentation is needed.** |
| **1.4** | **As a system admin, I want a configurable list of authoritative data sources (API endpoints, file feeds), so that we can add or replace providers without code changes.** |
| **1.5** | **As a developer, I want the verification engine to expose a RESTful `/verify` endpoint that returns a deterministic JSON report, so that downstream services can consume the results programmatically.** |

### Acceptance Criteria  

**1.1 – Flight Validation**  
- Input: airline code, flight number, departure date/time.  
- Engine queries the airline’s public schedule API (or cached feed).  
- Returns **`status: "valid"`** if flight exists and times match; otherwise **`status: "invalid"`** with a descriptive error.  
- Latency ≤ 500 ms for 95 % of requests (cached fallback after first call).  

**1.2 – Hotel Validation**  
- Input: hotel ID, check‑in/out dates.  
- Calls hotel’s availability endpoint (or uses nightly CSV feed).  
- Flags **over‑lap**, **unavailable**, or **price mismatch**.  
- Provides a link to the provider’s booking page for correction.  

**1.3 – Visa Requirement Check**  
- Input: passport nationality, destination country, travel dates.  
- Looks up the destination’s visa API (or static JSON rules).  
- Returns **`requires_visa: true/false`** and, if true, a list of required documents.  

**1.4 – Configurable Sources**  
- Admin UI (or YAML file) allows adding/removing sources with: `name`, `type` (REST, CSV, GraphQL), `auth`, `rate_limit`.  
- Changes are hot‑reloaded; no service restart required.  

**1.5 – `/verify` Endpoint**  
- `POST /verify` with payload `{ itinerary: [...], traveler: {...} }`.  
- Returns `{ itineraryId, results: [{ segmentId, status, messages }], overallStatus }`.  
- HTTP 200 on success, 4xx on malformed request, 5xx on internal error.  

---  

## Epic 2 – Enhanced Data Quality & Conflict Resolution

| # | User Story |
|---|------------|
| **2.1** | **As a traveler, I want the system to highlight mismatched time zones between flight legs, so that I can adjust connections and avoid missed flights.** |
| **2.2** | **As a traveler, I want a confidence score for each itinerary segment, so that I can prioritize which items need manual review.** |
| **2.3** | **As a support agent, I want to view a detailed audit log of all source queries for a verification run, so that I can troubleshoot disputes.** |
| **2.4** | **As a product owner, I want the engine to automatically suggest alternative flights/hotels when a segment is invalid, so that users can quickly correct their plans.** |

### Acceptance Criteria  

**2.1 – Time‑Zone Conflict Detection**  
- Detect when arrival time of segment A and departure time of segment B are in different zones and the layover is < minimum connection time (MCT) for that airport.  
- Flag with `type: "timezone_mismatch"` and suggest adding buffer time.  

**2.2 – Confidence Scoring**  
- Score 0–100 based on source reliability, freshness, and match completeness.  
- Expose `confidence` field in `/verify` response.  
- Scores ≥ 80 are considered “high confidence”.  

**2.3 – Audit Log**  
- Store each external request (URL, timestamp, response hash) in a searchable log DB.  
- Provide `GET /audit/{verificationId}` returning the full trace.  

**2.4 – Alternative Suggestions**  
- When a segment is `invalid`, query the same source for the next 3 viable alternatives (e.g., next flights, nearby hotels).  
- Return them in `suggestions` array with `price`, `duration`, and `link`.  

---  

## Epic 3 – Scalability, Monitoring & Compliance

| # | User Story |
|---|------------|
| **3.1** | **As a DevOps engineer, I want the service to auto‑scale based on request volume, so that latency stays low during peak travel seasons.** |
| **3.2** | **As a security auditor, I want all external API credentials to be stored in Vault and rotated automatically, so that we meet compliance standards.** |
| **3.3** | **As a product manager, I want real‑time dashboards showing verification success rates and source health, so that we can act on outages quickly.** |
| **3.4** | **As a data engineer, I want to persist raw source responses for 30 days, so that we can re‑run verifications for post‑mortem analysis.** |

### Acceptance Criteria  

**3.1 – Auto‑Scaling**  
- Deploy the engine in Kubernetes with HPA targeting 70 % CPU utilization.  
- Verify scaling up to 200 RPS without > 800 ms latency.  

**3.2 – Credential Management**  
- Integrate with HashiCorp Vault; all API keys fetched at runtime via side‑car injection.  
- Rotate keys every 30 days; failing rotation triggers alert and fallback to read‑only mode.  

**3.3 – Monitoring Dashboard**  
- Export Prometheus metrics: `verify_requests_total`, `verify_latency_seconds`, `source_error_rate`.  
- Grafana dashboard visualizes per‑source uptime, request volume, and overall success ratio.  

**3.4 – Raw Response Persistence**  
- Store each source response in an S3 bucket with lifecycle policy (30 days retention).  
- Link stored object ID in the audit log for easy retrieval.  

---  

## Epic 4 – User Experience & Internationalization (Stretch)

| # | User Story |
|---|------------|
| **4.1** | **As a non‑English speaking traveler, I want verification messages displayed in my native language, so that I understand issues clearly.** |
| **4.2** | **As a mobile app user, I want the verification to happen in the background and receive push notifications on issues, so that I’m alerted instantly.** |

### Acceptance Criteria  

**4.1 – i18n**  
- Support EN, ES, FR, ZH.  
- All user‑facing strings externalized to locale files.  
- API returns `messages` with `locale` field; client selects appropriate translation.  

**4.2 – Background Verification & Push**  
- Expose a webhook endpoint for third‑party apps to receive `verification_completed` events.  
- Include a `severity` flag (`info`, `warning`, `critical`).  
- Verify that push delivery latency ≤ 2 seconds after verification finishes.  

---  

### Prioritization for MVP  

1. **Epic 1** (Core Verification Engine) – all stories 1.1‑1.5.  
2. **Epic 2** – stories 2.1, 2.2, 2.3 (conflict detection, confidence, audit).  
3. **Epic 3** – story 3.1 (auto‑scaling) and 3.3 (monitoring) to ensure reliability.  
4. Remaining stories (2.4, 3.2‑3.4, 4.1‑4.2) are slated for post‑MVP releases.  

---  

*End of document.*
