# local-llm-investigative-journalism
DataHarvest 2026: How local LLMs can help you with sensitive information (a beginner's guide)

# Start here!

## Python and stuff

- Instal python and uv (https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)


## Install Ollama and/or LM Studio

### Windows
Powershell: irm https://ollama.com/install.ps1 | iex

### Mac 
curl -fsSL https://ollama.com/install.sh | sh

### Linux
curl -fsSL https://ollama.com/install.sh | sh

## Download a model

### For Ollama
- Open your terminal or Powershell
- Type: ollama list
- Type: ollama pull qwen3:4b

### For LM Studio
- Click on "Model Search" (top left)
- Search for Qwen3.5-4B-GGUF

## Get the code

Clone this repository. 
- In VS Code click on the top bar, click on "show and rund commands" and add the URL to this repository. Find a path on your computer to save it
- Create the virtual environment and install dependencies. Open the terminal in VS Code an type: "uv sync"
- Activate the virtual environment
  -- macOS / Linux: source .venv/bin/activate
  -- Windows: .venv\Scripts\activate