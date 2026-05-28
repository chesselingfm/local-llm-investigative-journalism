#%%
# pip install pypdf requests
# Make sure Ollama is running: ollama serve

#%%
import requests
from pypdf import PdfReader

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3-vl:8b"
PDF_PATH = "raw_files/EFTA02135382.pdf"

# Max characters sent per chunk to stay within model context window
CHUNK_SIZE = 6000


#%%
def extract_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def ask(prompt: str, model: str = MODEL) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["response"]


def analyze_pdf(pdf_path: str, question: str) -> str:
    text = extract_text(pdf_path)
    # Truncate to first chunk so we stay within context limits
    excerpt = text[:CHUNK_SIZE]
    prompt = (
        f"The following is an excerpt from a document:\n\n"
        f"---\n{excerpt}\n---\n\n"
        f"Question: {question}\n"
        f"Answer based only on the document content above."
    )
    return ask(prompt)


#%%
if __name__ == "__main__":
    question = "List all names, email adresses and dates you can find in this document."
    print(f"PDF: {PDF_PATH}")
    print(f"Question: {question}\n")
    answer = analyze_pdf(PDF_PATH, question)
    print(f"Answer:\n{answer}")

# %%
