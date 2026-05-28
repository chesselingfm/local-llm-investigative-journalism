#%%
# Make sure Ollama is running: ollama serve
# Requires Ollama >= 0.3 for structured output (format with JSON schema)

#%%
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"

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
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            "format": SCHEMA,
            "stream": False,
        },
    )
    response.raise_for_status()
    return json.loads(response.json()["message"]["content"])


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
