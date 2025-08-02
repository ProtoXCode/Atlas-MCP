import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"


async def query_ollama(prompt: str, model: str = "llama3") -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(OLLAMA_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "").strip()
