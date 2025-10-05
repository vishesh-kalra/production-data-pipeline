# Nginx Directory

This directory contains NGINX configuration files for reverse proxy and load balancing.

## Files

- `nginx.conf` - Main NGINX configuration file
- `ssl/` - Directory for SSL certificates (for HTTPS setup)

## Purpose

NGINX acts as a reverse proxy to:
- Route requests to the appropriate service (API or Dashboard)
- Handle SSL/TLS termination
- Provide load balancing if needed
- Serve static files efficiently

## Configuration

The nginx.conf file routes:
- `/api/*` requests to the FastAPI backend (port 8000)
- `/` requests to the Streamlit dashboard (port 8501)

## SSL Setup

For production, place your SSL certificates in the `ssl/` directory:
- `ssl/certificate.crt`
- `ssl/private.key`
