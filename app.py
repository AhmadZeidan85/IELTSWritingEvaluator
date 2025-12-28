import streamlit as st
import requests

MCP_ENDPOINT = "http://localhost:3333/tools/evaluate_writing"

st.set_page_config(page_title="IELTS Writing Evaluator")
st.title("📝 IELTS Writing Evaluator (MCP + RAG)")

essay = st.text_area(
    "Paste your IELTS essay below:",
    height=300,
    placeholder="Write your Task 1 or Task 2 essay..."
)

if st.button("Evaluate"):
    if not essay.strip():
        st.warning("Please enter an essay.")
    else:
        payload = {"essay": essay}

        with st.spinner("Evaluating..."):
            response = requests.post(MCP_ENDPOINT, json=payload)

        if response.status_code != 200:
            st.error("Error calling MCP server")
            st.text(response.text)
        else:
            result = response.json()

            st.success(f"Overall Band: {result['band']}")

            st.subheader("Sub-scores")
            st.write("Task Achievement:", result["task_achievement"])
            st.write("Coherence & Cohesion:", result["coherence"])
            st.write("Lexical Resource:", result["lexical"])
            st.write("Grammar:", result["grammar"])

            st.subheader("Examiner Feedback")
            st.write(result["feedback"])
