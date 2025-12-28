import streamlit as st
from mcp.client import MCPClient

st.set_page_config(page_title="IELTS Writing Evaluator")
st.title("📝 IELTS Writing Evaluator")

essay = st.text_area(
    "Paste your IELTS essay here",
    height=300,
    placeholder="Write your Task 1 or Task 2 essay..."
)

if st.button("Evaluate"):
    if not essay.strip():
        st.warning("Please enter an essay.")
    else:
        client = MCPClient("http://localhost:3333")
        result = client.call("evaluate_writing", {"essay": essay})

        st.success(f"Overall Band: {result['band']}")

        st.subheader("Sub-scores")
        st.write("Task Achievement:", result["task_achievement"])
        st.write("Coherence & Cohesion:", result["coherence"])
        st.write("Lexical Resource:", result["lexical"])
        st.write("Grammar:", result["grammar"])

        st.subheader("Examiner Feedback")
        st.write(result["feedback"])
