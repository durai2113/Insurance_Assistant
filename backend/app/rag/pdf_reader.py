"""Utilities for extracting text from uploaded PDF files."""

try:
    import fitz
except ImportError:  # pragma: no cover - handled at runtime
    fitz = None


def extract_text(pdf_path: str) -> str:
    """Extract all text from a PDF file."""

    if fitz is None:
        raise RuntimeError(
            "PyMuPDF is not installed. Install project dependencies to process "
            "uploaded PDFs."
        )

    document = fitz.open(pdf_path)
    text = ""

    for page in document:
        text += page.get_text()

    document.close()
    return text
