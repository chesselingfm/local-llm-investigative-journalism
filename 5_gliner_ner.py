#%%
# Install: uv add gliner
# GLiNER runs fully locally — no Ollama or LM Studio needed

#%%
from gliner import GLiNER

MODEL = "urchade/gliner_medium-v2.1"  # downloads automatically on first run

model = GLiNER.from_pretrained(MODEL)


def extract_entities(text: str, labels: list[str]) -> list[dict]:
    return model.predict_entities(text, labels)


#%%
if __name__ == "__main__":
    text = (
        "Jeffrey Epstein, a financier with ties to Ghislaine Maxwell, "
        "was arrested in July 2019 at Teterboro Airport in New Jersey. "
        "His alleged victims included minors recruited in Palm Beach, Florida. "
        "Prosecutors from the Southern District of New York led the case."
    )

    labels = ["PERSON", "ORGANIZATION", "LOCATION", "DATE"]

    print(f"Text:\n{text}\n")
    print(f"Entity types: {labels}\n")

    entities = extract_entities(text, labels)

    for entity in entities:
        print(f"  [{entity['label']}] {entity['text']}  (score: {entity['score']:.2f})")

# %%
