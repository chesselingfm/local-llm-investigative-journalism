#%%
# pip install openai
# In LM Studio: Local Server tab → Start Server, then load qwen3-vl model

#%%
import base64
from pathlib import Path
from openai import OpenAI

LM_STUDIO_URL = "http://localhost:1234/v1"
MODEL = "qwen3-vl"  # match the vision model loaded in LM Studio
IMAGE_PATH = "raw_files/EFTA00248387_p21_xref_378.png"

client = OpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio")


#%%
def encode_image(image_path: str) -> tuple[str, str]:
    path = Path(image_path)
    suffix = path.suffix.lower().lstrip(".")
    mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8"), mime


def ask_about_image(image_path: str, question: str, model: str = MODEL) -> str:
    b64, mime = encode_image(image_path)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an investigative journalism assistant. "
                    "Analyze images carefully and extract all relevant information."
                ),
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/{mime};base64,{b64}"},
                    },
                ],
            },
        ],
        timeout=120,
    )
    return response.choices[0].message.content


#%%
if __name__ == "__main__":
    question = "Describe this image in detail. List all text, names, numbers, dates and any other information you can find."
    print(f"Image: {IMAGE_PATH}")
    print(f"Question: {question}\n")
    answer = ask_about_image(IMAGE_PATH, question)
    print(f"Answer:\n{answer}")

# %%
