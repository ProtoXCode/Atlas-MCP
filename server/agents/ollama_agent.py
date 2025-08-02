from .ollama_client import query_ollama


async def scan_network(area: str = 'Line A') -> str:
    prompt_text = (
        f"You are an industrial AI assistant. You just scanned the area '{area}'. "
        f"Invent 3 realistic devices you might find in an industrial factory. "
        f"Give each a type, vendor, and model. Keep it short and human readable."
    )
    return await query_ollama(prompt_text)
