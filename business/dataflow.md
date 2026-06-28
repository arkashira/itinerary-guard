```markdown
# Dataflow Architecture for Itinerary-Guard

## External Data Sources
- **Flight APIs**: Real-time flight information (e.g., FlightAware, Amadeus)
- **Hotel APIs**: Booking and availability data (e.g., Booking.com, Expedia)
- **Weather APIs**: Current and forecasted weather conditions (e.g., OpenWeatherMap)
- **Transport APIs**: Public transport schedules and disruptions (e.g., Transit API)
- **Government Data**: Travel advisories and regulations (e.g., CDC, State Department)

## Ingestion Layer
- **API Gateway**: Manages incoming requests and routes them to appropriate services.
- **Data Collector**: Fetches data from external APIs at defined intervals.
- **Webhook Listener**: Receives real-time updates from partners and external sources.

## Processing/Transform Layer
- **Data Validator**: Checks the integrity and accuracy of incoming data.
- **Data Normalizer**: Converts data into a consistent format for processing.
- **Cross-Checker**: Compares itinerary data against multiple sources to identify inconsistencies.
- **Alert Generator**: Flags discrepancies and generates alerts for further action.

## Storage Tier
- **Relational Database**: Stores structured itinerary data and user profiles (e.g., PostgreSQL).
- **NoSQL Database**: Stores unstructured data and logs (e.g., MongoDB).
- **Cache Layer**: In-memory data store for quick access to frequently requested data (e.g., Redis).

## Query/Serving Layer
- **GraphQL API**: Provides a flexible API for clients to query itinerary data and alerts.
- **REST API**: Legacy API for backward compatibility with existing clients.
- **Authentication Service**: Manages user authentication and authorization (e.g., OAuth 2.0).

## Egress to User
- **Web Application**: User interface for travelers to input itineraries and view alerts.
- **Mobile Application**: Native app for real-time notifications and itinerary management.
- **Email/SMS Notification Service**: Sends alerts and updates to users about their itineraries.

```

### ASCII Block Diagram

```
+---------------------+
|  External Data      |
|      Sources        |
|---------------------|
| Flight APIs         |
| Hotel APIs          |
| Weather APIs        |
| Transport APIs      |
| Government Data     |
+----------+----------+
           |
           v
+---------------------+
|   Ingestion Layer   |
|---------------------|
| API Gateway         |
| Data Collector      |
| Webhook Listener    |
+----------+----------+
           |
           v
+---------------------+
| Processing/Transform|
|        Layer        |
|---------------------|
| Data Validator      |
| Data Normalizer     |
| Cross-Checker       |
| Alert Generator      |
+----------+----------+
           |
           v
+---------------------+
|     Storage Tier    |
|---------------------|
| Relational Database  |
| NoSQL Database      |
| Cache Layer         |
+----------+----------+
           |
           v
+---------------------+
|  Query/Serving Layer|
|---------------------|
| GraphQL API        |
| REST API           |
| Authentication      |
+----------+----------+
           |
           v
+---------------------+
|   Egress to User    |
|---------------------|
| Web Application      |
| Mobile Application   |
| Email/SMS Service    |
+---------------------+
```