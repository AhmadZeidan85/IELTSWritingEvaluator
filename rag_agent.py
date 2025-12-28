from typing import List
from dataclasses import dataclass
import json
import numpy as np
import faiss
import torch

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


@dataclass
class EvalResult:
    band: float
    task_achievement: float
    coherence: float
    lexical: float
    grammar: float
    feedback: str


class IELTSWritingEvaluator:
    def __init__(self, rubric_docs: List[str]):
        # -------- RAG Embeddings --------
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.rubric_docs = rubric_docs
        self.index = self._build_index(rubric_docs)

        # -------- Codespaces-safe LLM --------
        self.model_name = "Qwen/Qwen2.5-3B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto",
            torch_dtype=torch.float16
        )

        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer
        )

    def _build_index(self, docs: List[str]):
        vectors = self.embedder.encode(docs)
        index = faiss.IndexFlatL2(vectors.shape[1])
        index.add(np.array(vectors))
        return index

    def retrieve(self, essay: str, k: int = 3) -> List[str]:
        q_vec = self.embedder.encode([essay])
        _, ids = self.index.search(np.array(q_vec), k)
        return [self.rubric_docs[i] for i in ids[0]]

    def evaluate(self, essay: str) -> EvalResult:
        context = self.retrieve(essay)

        prompt = f"""
You are an official IELTS Writing examiner.

Evaluate the essay using the rubric context below.

Return STRICT JSON ONLY in this format:
{{
  "band": number,
  "task_achievement": number,
  "coherence": number,
  "lexical": number,
  "grammar": number,
  "feedback": string
}}

Rubric Context:
{context}

Essay:
{essay}
"""

        output = self.generator(
            prompt,
            max_new_tokens=512,
            do_sample=False,
            temperature=0.0
        )

        raw = output[0]["generated_text"].replace(prompt, "").strip()

        try:
            data = json.loads(raw)
        except Exception:
            raise ValueError(f"Invalid JSON from model:\\n{raw}")

        return EvalResult(**data)
