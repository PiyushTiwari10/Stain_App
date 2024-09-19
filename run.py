import subprocess
import sys
import streamlit as st

# Streamlit info (optional)
st.title("Stain Detection API Service")

st.write("""
This is an API service for stain detection. The FastAPI backend is running and ready to serve requests.
""")

# Run FastAPI using Uvicorn in the background
process = subprocess.Popen([sys.executable, "-m", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"])

st.write("API is running at http://localhost:8000/detect_stain")

# Wait for process to terminate (optional)
process.wait()
