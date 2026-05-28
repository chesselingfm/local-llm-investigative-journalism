#%%
# Make sure Ollama is running
!ollama serve


#%%
# Show all 
!ollama list


#%%
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:4b"  # change to any model you have pulled


def ask(prompt: str, model: str = MODEL) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "stream": False},
    )
    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    question = "Who is currently the French president, the British Prime Minister, the German Chancellor and the Queen or King of Denmark?"
    print(f"Question: {question}\n")
    answer = ask(question)
    print(f"Answer:\n{answer}")

# %%
