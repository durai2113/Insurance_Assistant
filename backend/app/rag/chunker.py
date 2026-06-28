"""Utilities for splitting source text into retrievable chunks."""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text: str):
    """Split text into overlapping chunks for downstream retrieval."""

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_text(text)
