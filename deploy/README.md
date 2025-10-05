# Deploy Directory

This directory contains deployment scripts and configuration files for different cloud platforms.

## Cloud Platform Scripts

- `oracle-cloud-setup.sh` - Setup script for Oracle Cloud Always Free Tier
- `aws-setup.sh` - Setup script for AWS Free Tier
- `azure-setup.sh` - Setup script for Azure Free Tier

## Prerequisites

- Docker and Docker Compose installed on target server
- Cloud account with appropriate permissions
- SSH access to the cloud instance

## Deployment Steps

1. Clone this repository to your cloud instance
2. Copy `.env.example` to `.env` and fill in your credentials
3. Run the appropriate setup script for your cloud platform
4. Access your dashboard at `http://your-server-ip:8501`
5. Access API documentation at `http://your-server-ip:8000/docs`
