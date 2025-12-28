from mcp.server.fastmcp import FastMCP
from rag_agent import IELTSWritingEvaluator

rubric_docs = [
    "Task Achievement: addresses all parts of the task with a clear position",
    "Coherence and Cohesion: logical organization and paragraphing",
    "Lexical Resource: range and accuracy of vocabulary",
    "Grammatical Range and Accuracy: sentence variety and correctness"
]

evaluator = IELTSWritingEvaluator(rubric_docs)

mcp = FastMCP("IELTS Writing Evaluator")


@mcp.tool()
def evaluate_writing(essay: str) -> dict:
    """
    Evaluate an IELTS writing essay.
    """
    result = evaluator.evaluate(essay)
    return result.__dict__
