# Technical Specification
=========================

## Overview
-----------

itinerary-guard is a real-time travel-info verification service that cross-checks itineraries against multiple authoritative sources and flags inconsistencies before booking. This document outlines the technical specification for the project.

## Architecture Overview
------------------------

The architecture of itinerary-guard consists of the following components:

### 1. API Gateway

*   Responsible for receiving incoming requests from clients
*   Handles authentication and authorization
*   Routes requests to the appropriate microservice

### 2. Itinerary Validator

*   Responsible for validating itineraries against multiple authoritative sources
*   Utilizes a graph database to store and query itinerary data
*   Performs real-time cross-checking of itinerary information

### 3. Data Ingestion Service

*   Responsible for ingesting data from authoritative sources
*   Utilizes web scraping and API integration to collect data
*   Stores data in the graph database

### 4. Notification Service

*   Responsible for sending notifications to clients when inconsistencies are detected
*   Utilizes a message queue to handle notifications

## Data Model
-------------

The data model for itinerary-guard consists of the following entities:

### 1. Itinerary

*   Represents a travel itinerary
*   Has attributes for departure and arrival airports, flight numbers, and travel dates

### 2. Flight

*   Represents a flight
*   Has attributes for flight number, departure and arrival airports, and travel dates

### 3. Airport

*   Represents an airport
*   Has attributes for airport code and name

## Key APIs/Interfaces
------------------------

The following APIs/interfaces are key to the functionality of itinerary-guard:

### 1. Itinerary Validation API

*   Accepts an itinerary as input and returns a validation result
*   Utilizes the Itinerary Validator component

### 2. Data Ingestion API

*   Accepts data from authoritative sources and ingests it into the graph database
*   Utilizes the Data Ingestion Service component

### 3. Notification API

*   Sends notifications to clients when inconsistencies are detected
*   Utilizes the Notification Service component

## Tech Stack
-------------

The tech stack for itinerary-guard consists of the following components:

### 1. Programming Language

*   Python 3.9+

### 2. Framework

*   FastAPI

### 3. Database

*   Graph database (e.g. Neo4j)

### 4. Message Queue

*   Apache Kafka

### 5. Web Scraping Library

*   Scrapy

## Dependencies
--------------

The following dependencies are required for itinerary-guard:

### 1. FastAPI

*   `fastapi==0.92.0`

### 2. Graph Database Driver

*   `neo4j==4.2.0`

### 3. Message Queue Client

*   `confluent-kafka==5.4.0`

## Deployment
-------------

itinerary-guard will be deployed on a cloud-based platform (e.g. AWS). The following components will be deployed separately:

### 1. API Gateway

*   Deployed as a containerized application on a load balancer

### 2. Itinerary Validator

*   Deployed as a containerized application on a separate server

### 3. Data Ingestion Service

*   Deployed as a containerized application on a separate server

### 4. Notification Service

*   Deployed as a containerized application on a separate server

### 5. Database

*   Deployed as a managed service on the cloud platform

### 6. Message Queue

*   Deployed as a managed service on the cloud platform
