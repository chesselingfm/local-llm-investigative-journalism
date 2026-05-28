#%%
# Make sure LM Studio is running with the local server enabled (port 1234)
# Enable "Structured Output" in LM Studio server settings

#%%
import json
from openai import OpenAI

LM_STUDIO_URL = "http://localhost:1234/v1"
MODEL = "qwen/qwen3-8b"  # match the model loaded in LM Studio

client = OpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio")

SCHEMA = {
    "type": "object",
    "properties": {
        "persons":       {"type": "array", "items": {"type": "string"}},
        "organizations": {"type": "array", "items": {"type": "string"}},
        "locations":     {"type": "array", "items": {"type": "string"}},
        "dates":         {"type": "array", "items": {"type": "string"}},
        "key_claims":    {"type": "array", "items": {"type": "string"}},
        "summary":       {"type": "string"},
    },
    "required": ["persons", "organizations", "locations", "dates", "key_claims", "summary"],
}

SYSTEM_PROMPT = (
    "You are an investigative journalism assistant. "
    "Extract structured information from the given text. "
    "Return only valid JSON matching the schema — no commentary."
)


def analyze(text: str, model: str = MODEL) -> dict:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "analysis", "strict": True, "schema": SCHEMA},
        },
    )
    return json.loads(response.choices[0].message.content)


#%%
if __name__ == "__main__":
    text = (
        "Jeffrey Epstein, a financier with ties to Ghislaine Maxwell, "
        "was arrested in July 2019 at Teterboro Airport in New Jersey. "
        "His alleged victims included minors recruited in Palm Beach, Florida. "
        "Prosecutors from the Southern District of New York led the case. "
        "Former President Bill Clinton and Prince Andrew were listed among his associates."
    )

    print(f"Input text:\n{text}\n")
    result = analyze(text)
    print("Structured output:")
    print(json.dumps(result, indent=2))

# %%
