# breakeven.md

## Unit Economics & Break-even Analysis for Itinerary-Guard

### Cost per Active User
1. **Compute Costs**: 
   - Estimated monthly compute cost per user: $0.50
   - Annual compute cost per user: $6.00

2. **Storage Costs**: 
   - Estimated monthly storage cost per user: $0.10
   - Annual storage cost per user: $1.20

3. **Bandwidth Costs**: 
   - Estimated monthly bandwidth cost per user: $0.20
   - Annual bandwidth cost per user: $2.40

**Total Monthly Cost per Active User**:  
Compute + Storage + Bandwidth = $0.50 + $0.10 + $0.20 = **$0.80**  
**Total Annual Cost per Active User**: $6.00 + $1.20 + $2.40 = **$9.60**

### Pricing Tiers
| Tier Name         | Monthly Price ($) | Features                                                                 |
|-------------------|-------------------|--------------------------------------------------------------------------|
| Basic             | $10               | Real-time itinerary verification, Email alerts for inconsistencies       |
| Pro               | $25               | All Basic features + SMS alerts, Priority support, 5 simultaneous users  |
| Enterprise        | $50               | All Pro features + Custom integrations, API access, 20 simultaneous users |

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: **$20 - $50** per user
  - Marketing spend, promotional offers, and sales efforts will influence this range.

### Lifetime Value (LTV) Estimate
- Average user lifespan: 24 months
- Average revenue per user (ARPU) for each tier:
  - Basic: $10 x 24 = **$240**
  - Pro: $25 x 24 = **$600**
  - Enterprise: $50 x 24 = **$1200**

- LTV Calculation:
  - Basic: LTV = $240 - CAC (assuming $35) = **$205**
  - Pro: LTV = $600 - CAC (assuming $35) = **$565**
  - Enterprise: LTV = $1200 - CAC (assuming $35) = **$1165**

### Break-even Users Count
- Monthly Fixed Costs (e.g., salaries, infrastructure): **$5,000**
- Contribution Margin per User:
  - Basic: $10 - $0.80 = **$9.20**
  - Pro: $25 - $0.80 = **$24.20**
  - Enterprise: $50 - $0.80 = **$49.20**

**Break-even Users Count**:
- Basic: $5,000 / $9.20 ≈ **544 users**
- Pro: $5,000 / $24.20 ≈ **207 users**
- Enterprise: $5,000 / $49.20 ≈ **102 users**

### Path to $10K MRR
- Target Monthly Recurring Revenue (MRR): **$10,000**
- Pricing Tier Strategy:
  - **Combination of Pro and Enterprise Tiers**:
    - Pro Tier: 200 users x $25 = $5,000
    - Enterprise Tier: 100 users x $50 = $5,000
    - Total MRR = $10,000

**Summary**: To reach $10K MRR, we can target **200 Pro users** and **100 Enterprise users**.