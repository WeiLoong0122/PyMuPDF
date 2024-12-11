# pylint: disable=wildcard-import,unused-import
import fitz  # PyMuPDF

def extract_vector_and_text_from_pdf(~/Downloads/2024-12-10 TOPAZ PILING  LAYOUT (Phase 1 & 2)_WITH SCHEDULE_120%.pdf):
    doc = fitz.open(~/Downloads/2024-12-10 TOPAZ PILING  LAYOUT (Phase 1 & 2)_WITH SCHEDULE_120%.pdf)
    text_elements = []
    vector_elements = []
