import os
import json
import requests

class IELTSWritingAgent:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY","ybMAvProEnsVMuNV1Kw10L9G7pmjDhXR")
        if not self.api_key:
            print("⚠️ MISTRAL_API_KEY is not set. MCP will start, but evaluation will return error.")
        self.endpoint = "https://api.mistral.ai/v1/chat/completions"
        self.model = "mistral-small"

        self.descriptors = """
IELTS Writing Task 1 Band Descriptors:
- Task Achievement
- Coherence & Cohesion
- Lexical Resource
- Grammar
"""

    def evaluate(self, essay: str) -> dict:
        if not self.api_key:
            return {"error": "MISTRAL_API_KEY is not set"}

        prompt = f"""
Evaluate this IELTS Task 1 response.
Return JSON only.

Essay:
{essay}
"""
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"model": self.model, "messages":[{"role":"user","content":prompt}],"temperature":0.3}

        r = requests.post(self.endpoint, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"]
        print(f"[DEBUG] Received content: {content}")
        json_text = content[content.find("{"):content.rfind("}")+1]
        print(f"[DEBUG] Received content: {json_text}")
        return json.loads(json_text)
