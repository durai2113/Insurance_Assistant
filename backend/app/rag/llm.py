"""Helpers for creating Groq-backed answers from prompts."""

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

try:
    from groq import Groq
except ImportError:  # pragma: no cover - handled at runtime
    Groq = None


@lru_cache(maxsize=1)
def get_client():
    """Return a cached Groq client instance."""

    if Groq is None:
        raise RuntimeError(
            "groq is not installed. Install project dependencies to generate answers."
        )

    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY is not configured.")

    return Groq(api_key=GROQ_API_KEY)


def generate_answer(prompt: str) -> str:
    """Generate an answer for the provided prompt."""

    response = get_client().chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=512,
    )

    return response.choices[0].message.content.strip()
