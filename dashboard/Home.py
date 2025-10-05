import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Multi-Industry Data Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API configuration
API_BASE_URL = "http://api-backend:8000/api/v1"

# Dashboard title
st.title("📊 Multi-Industry Data Dashboard")
st.markdown("Real-time analytics for Finance, Healthcare, and Supply Chain")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    industry = st.selectbox("Select Industry", ["All", "Finance", "Healthcare", "Supply Chain"])
    date_range = st.date_input(
        "Date Range", 
        [datetime.now() - timedelta(days=30), datetime.now()]
    )
    
    if st.button("🔄 Refresh Data"):
        st.rerun()

# Fetch overview data
try:
    response = requests.get(f"{API_BASE_URL}/dashboard/overview", timeout=5)
    if response.status_code == 200:
        data = response.json()
        
        # Key metrics row
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", data.get("total_records", 0))
        with col2:
            st.metric("Finance Data", data.get("finance_records", 0))
        with col3:
            st.metric("Healthcare Data", data.get("healthcare_records", 0))
        with col4:
            st.metric("Supply Chain Data", data.get("supply_chain_records", 0))
        
        st.divider()
        
        # Data quality section
        st.subheader("System Status")
        st.success("✅ All systems operational")
        st.info(f"Last updated: {data.get('last_updated', 'N/A')}")
        
    else:
        st.error("Failed to fetch data from API")
except requests.exceptions.ConnectionError:
    st.error("❌ Cannot connect to API backend. Make sure the API service is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Footer
st.divider()
st.caption("Production Data Pipeline Dashboard | Multi-Industry Analytics Platform")
