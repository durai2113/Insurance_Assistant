"""Prompt construction helpers for the RAG answer generator."""


def build_prompt(question: str, chunks: list[str]) -> str:
    """Build the final prompt from retrieved chunks and the user question."""

    context = "\n\n".join(chunks)

    return f"""
You are an Insurance Policy Assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
reply:

"I couldn't find the answer in the uploaded document."

Context:
---------
{context}

---------

Question:
{question}

Answer:
"""
