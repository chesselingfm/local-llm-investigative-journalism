#%%
# pip install pypdf openai
# In LM Studio: Local Server tab → Start Server, then load your model

#%%
from openai import OpenAI
from pypdf import PdfReader

LM_STUDIO_URL = "http://localhost:1234/v1"
MODEL = "qwen3:4b"  # match the model loaded in LM Studio
PDF_PATH = "raw_files/EFTA02135382.pdf"

# Max characters sent per chunk to stay within model context window
CHUNK_SIZE = 6000

client = OpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio")


#%%
def extract_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def ask(system: str, user: str, model: str = MODEL) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        timeout=120,
    )
    return response.choices[0].message.content


def analyze_pdf(pdf_path: str, question: str) -> str:
    text = extract_text(pdf_path)
    excerpt = text[:CHUNK_SIZE]
    system = (
        "You are an investigative journalism assistant. "
        "Answer questions strictly based on the provided document excerpt."
    )
    user = (
        f"Document excerpt:\n\n---\n{excerpt}\n---\n\n"
        f"Question: {question}"
    )
    return ask(system, user)


#%%
if __name__ == "__main__":
    question = "List all names, email adresses and dates you can find in this document."
    print(f"PDF: {PDF_PATH}")
    print(f"Question: {question}\n")
    answer = analyze_pdf(PDF_PATH, question)
    print(f"Answer:\n{answer}")

# %%
