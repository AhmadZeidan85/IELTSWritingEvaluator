
import os
import streamlit as st
import requests
import json

# Use Codespaces forwarded public URL if available
MCP_URL = os.getenv(
    "MCP_URL",
    "https://fictional-journey-4v9r9xp4wxw3jrj6-3333.app.github.dev/tools/evaluate_writing"
)

st.set_page_config(page_title="IELTS Task 1 Evaluator")
st.title("📝 IELTS Task 1 Writing Evaluator (Mistral API)")

essay = st.text_area("Paste your Task 1 response", height=300)

if st.button("Evaluate"):
    with st.spinner("Sending request to MCP server..."):
        # Prepare the request payload
        payload = {"essay": essay}
        st.subheader("📤 Request JSON:")
        st.json(payload)  # Display request being sent

        try:
            r = requests.post(MCP_URL, json=payload, timeout=120)
            if r.status_code == 200:
                st.subheader("📥 Response JSON:")
                st.json(r.json())  # Display the result from MCP server
            else:
                st.error(f"Server returned status {r.status_code}: {r.text}")
        except Exception as e:
            st.error(f"Failed to connect to MCP server: {e}")
