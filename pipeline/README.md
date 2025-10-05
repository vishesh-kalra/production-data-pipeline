# Pipeline Directory

This directory contains the data pipeline workers for ingesting data from external APIs.

## Structure

- `scheduler.py` - Main scheduler for running data ingestion jobs
- `api_client.py` - API client for connecting to external data sources
- `postgres_handler.py` - Database handler for PostgreSQL
- `mongo_handler.py` - Database handler for MongoDB
- `Dockerfile` - Container configuration for pipeline services
- `requirements.txt` - Python dependencies

## Industry-Specific Pipelines

- **Finance**: Fetches data from Yahoo Finance, Alpha Vantage, IEX Cloud
- **Healthcare**: Fetches data from OpenFDA, HealthData.gov, PubMed  
- **Supply Chain**: Fetches data from IMF, OECD, World Bank

## Configuration

Set the `INDUSTRY` environment variable to specify which pipeline to run:
- `finance`
- `healthcare`
- `supply_chain`
