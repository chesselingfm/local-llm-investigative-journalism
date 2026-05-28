#%%
# Make sure LM Studio is running with the local server enabled (port 1234)

#%%
from openai import OpenAI

LM_STUDIO_URL = "http://localhost:1234/v1"
MODEL = "qwen/qwen3-8b"  # match the model loaded in LM Studio

client = OpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio")


def ask(prompt: str, model: str = MODEL) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


#%%
if __name__ == "__main__":
    question = "Who is currently the French president, the British Prime Minister, the German Chancellor and the Queen or King of Denmark?"
    print(f"Question: {question}\n")
    answer = ask(question)
    print(f"Answer:\n{answer}")

# %%
