from mcp.server.fastmcp import FastMCP
from rag_agent import IELTSWritingAgent

mcp = FastMCP("IELTS Task 1 Writing Evaluator")
agent = IELTSWritingAgent()

@mcp.tool()
def evaluate_writing(essay: str) -> dict:
    """
    Evaluate IELTS Writing Task 1 using Mistral API
    """
    return agent.evaluate(essay)
