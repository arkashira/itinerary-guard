# Business Model Canvas – Itinerary‑Guard
**Product:** Real‑time travel‑info verification service that cross‑checks user‑submitted itineraries against multiple authoritative sources (airlines, hotels, rail operators, government travel advisories) and flags inconsistencies before booking.  
**Repository:** `itinerary-guard` (Axentx product)

---

## 1. Value Proposition
| What we deliver | Why it matters |
|-----------------|----------------|
| **Instant itinerary validation** – Detect mismatched flight numbers, dates, airport codes, visa requirements, and COVID‑19 restrictions in milliseconds. | Prevents costly re‑bookings, missed connections, and compliance penalties. |
| **Multi‑source authority aggregation** – Pulls data from airline APIs, GDS, hotel PMS, government travel advisories, and third‑party aggregators. | Guarantees the most up‑to‑date, trustworthy information. |
| **Seamless integration** – SDKs & REST/WebSocket endpoints for booking engines, travel agencies, and consumer‑facing apps. | Reduces dev effort; plug‑and‑play for existing platforms. |
| **Compliance & risk reduction** – Automated flagging of visa, health, and security alerts. | Helps partners meet regulatory obligations and protect brand reputation. |
| **Scalable, low‑latency architecture** – Built on vLLM inference engine + SGLang structured generation for fast rule‑based and LLM‑augmented checks. | Handles high‑volume booking spikes without degrading user experience. |

---

## 2. Customer Segments
| Primary | Secondary |
|---------|-----------|
| **Online Travel Agencies (OTAs)** – Booking.com, Expedia, Skyscanner | **Airlines & Hotel Chains** – Direct booking portals needing pre‑flight validation |
| **Corporate Travel Management platforms** – SAP Concur, TripActions | **Travel Insurance providers** – Need accurate itinerary data for underwriting |
| **Consumer travel apps** – Mobile itinerary planners, trip‑sharing services | **Regulatory bodies / Government portals** – Offer validation as a public service |

---

## 3. Channels
| Channel | Description |
|---------|-------------|
| **Direct API sales** – Subscription contracts with API keys, tiered usage plans. |
| **Marketplace integration** – Publish SDKs on npm, PyPI, Maven Central; promote via developer portals. |
| **Partner co‑sell** – Joint go‑to‑market with GDS providers (Amadeus, Sabre) and airline alliances. |
| **Developer evangelism** – Hackathons, webinars, technical blog posts, sample code in repo. |
| **Enterprise sales team** – Target large OTAs and corporate travel platforms with custom SLAs. |

---

## 4. Revenue Streams
| Stream | Pricing Model | Notes |
|--------|---------------|-------|
| **Usage‑based API** – Pay‑per‑validation (e.g., $0.001 per check) with volume discounts. | Scales with transaction volume; aligns cost with value. |
| **Tiered subscription** – Monthly flat‑fee for up‑to‑X validations (Starter, Professional, Enterprise). | Predictable revenue; includes SLA guarantees. |
| **Premium data add‑ons** – Real‑time government advisory feeds, visa‑eligibility engine. | Higher margin; optional per‑partner. |
| **Professional services** – Integration consulting, custom rule‑engine development. | One‑off fees; upsell path to higher tier. |
| **Revenue share** – Joint product with GDS/airline partners (e.g., 5 % of booking value saved by avoiding re‑book). | Incentivizes partners to adopt. |

---

## 5. Cost Structure
| Cost Category | Key Items |
|---------------|-----------|
| **Cloud infrastructure** – Compute (vLLM + SGLang), storage for cached authority data, CDN for low‑latency API. |
| **Data licensing** – Fees for airline schedules, hotel inventory feeds, government advisory APIs. |
| **R&D & engineering** – Salaries for backend, ML, dev‑ops, and QA teams; open‑source contributions (vLLM, SGLang). |
| **Compliance & legal** – Data protection (GDPR, CCPA) audits, licensing agreements. |
| **Sales & marketing** – Partner commissions, developer outreach, conference sponsorships. |
| **Support & SLA** – 24/7 technical support, incident response tooling. |

---

## 6. Key Resources
| Resource | Role |
|----------|------|
| **vLLM inference engine** – High‑throughput, low‑latency model serving for LLM‑augmented validation rules. |
| **SGLang structured generation** – Guarantees deterministic output for rule checks and explanations. |
| **Authority data pipelines** – Automated ETL from airline GDS, hotel PMS, government APIs. |
| **PGVector knowledge store** – Stores embeddings of itinerary patterns, historical validation outcomes for fast similarity search. |
| **SDKs & client libraries** – JavaScript, Python, Java, Swift packages for easy integration. |
| **Team expertise** – Domain experts in travel regulations, ML engineers, API product managers. |

---

## 7. Key Activities
| Activity | Description |
|----------|-------------|
| **Data ingestion & normalization** – Continuous sync with airline, hotel, and government sources; schema mapping. |
| **Model training & fine‑tuning** – Use Axentx’s 22M+ auto‑pairs + 7M instruction‑response pairs to train validation LLMs. |
| **API development & scaling** – Deploy vLLM + SGLang services behind load balancers; implement rate‑limiting & quota management. |
| **Compliance monitoring** – Keep authority data up‑to‑date with regulatory changes; audit logs for each validation. |
| **Partner integration** – Build and maintain connectors for major OTAs, GDS, and corporate travel platforms. |
| **Customer success & support** – Onboarding, SLA monitoring, incident resolution. |
| **Feedback loop** – Capture false‑positive/negative cases, feed back into model retraining and rule updates. |

---

## 8. Key Partners
| Partner | Value to Itinerary‑Guard |
|---------|--------------------------|
| **Airline & hotel data providers** (Amadeus, Sabre, Travelport, Hotelbeds) | Authoritative schedule & inventory feeds. |
| **Government agencies** (IATA, ICAO, national travel ministries) | Official travel advisories, visa & health regulations. |
| **Cloud providers** (AWS, GCP, Azure) | Scalable compute for vLLM/SGLang, managed PGVector. |
| **Compliance consultants** | Ensure GDPR/CCPA compliance, data licensing. |
| **Developer community** – Open‑source contributors to vLLM & SGLang | Improves core engine, drives adoption. |
| **Payment processors** (Stripe, Braintree) | Handles subscription & usage billing. |

---

### Summary
Itinerary‑Guard turns fragmented travel data into a single, real‑time validation service that saves OTAs, airlines, and corporate travel platforms millions in re‑booking costs and regulatory fines. By leveraging Axentx’s proven LLM infrastructure (vLLM, SGLang) and a robust multi‑source data pipeline, the product can be monetized through usage‑based APIs, tiered subscriptions, and premium data add‑ons while maintaining a lean cost structure focused on cloud, data licensing, and high‑impact engineering.
