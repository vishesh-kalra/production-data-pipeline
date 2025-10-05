-- Database initialization script for production data pipeline
-- This script creates separate databases for each industry

-- Finance database
CREATE DATABASE IF NOT EXISTS finance_db;

-- Healthcare database
CREATE DATABASE IF NOT EXISTS healthcare_db;

-- Supply chain database
CREATE DATABASE IF NOT EXISTS supply_chain_db;

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE finance_db TO admin;
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO admin;
GRANT ALL PRIVILEGES ON DATABASE supply_chain_db TO admin;
