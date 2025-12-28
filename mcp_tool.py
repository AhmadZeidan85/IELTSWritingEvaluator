from mcp.server.fastmcp import FastMCP
from rag_agent import IELTSWritingEvaluator

rubric_docs = [
    "Task Achievement: addresses all parts of the task with a clear position",
    "Coherence and Cohesion: logical organization, clear paragraphing",
    "Lexical Resource: wide vocabulary with appropriate usage",
    "Grammatical Range and Accuracy: variety of sentence structures"
]

evaluator = IELTSWritingEvaluator(rubric_docs)

mcp = FastMCP("IELTS Writing Evaluator MCP")


@mcp.tool()
def evaluate_writing(essay: str) -> dict:
    """
    Evaluate an IELTS writing essay and return band scores.
    """
    result = evaluator.evaluate(essay)
    return result.__dict__
