# pylint: disable=wildcard-import,unused-import
import fitz  # PyMuPDF

def extract_vector_and_text_from_pdf(~/Downloads/2024-12-10 TOPAZ PILING  LAYOUT (Phase 1 & 2)_WITH SCHEDULE_120%.pdf):
    doc = fitz.open(~/Downloads/2024-12-10 TOPAZ PILING  LAYOUT (Phase 1 & 2)_WITH SCHEDULE_120%.pdf)
    text_elements = []
    vector_elements = []
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(1)
        
        # Extract vector graphics (lines, shapes, etc.)
        vector_elements.append(page.get_drawings())  # List of drawing elements (e.g., lines, arrows)
        
        # Extract text (potentially the labels)
        text_elements.append(page.get_text("text"))
    
    return vector_elements, text_elements
