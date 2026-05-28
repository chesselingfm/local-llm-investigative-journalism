#%%
# pip install requests
# Make sure Ollama is running: ollama serve
# Pull the model: ollama pull qwen3-vl:8b (or the variant you have)

#%%
import base64
from pathlib import Path
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3-vl:8b"
IMAGE_PATH = "raw_files/EFTA00248387_p21_xref_378.png"


#%%
def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def ask_about_image(image_path: str, question: str, model: str = MODEL) -> str:
    b64 = encode_image(image_path)
    prompt = (
        f"{question}\n\n"
        "Describe all text, names, numbers, dates and visual elements you can see."
    )
    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "images": [b64], "stream": False},
        timeout=180,
    )
    response.raise_for_status()
    return response.json()["response"]


#%%
if __name__ == "__main__":
    question = "Describe this image in detail. List all text, names, numbers, dates and any other information you can find."
    print(f"Image: {IMAGE_PATH}")
    print(f"Question: {question}\n")
    answer = ask_about_image(IMAGE_PATH, question)
    print(f"Answer:\n{answer}")

# %%
