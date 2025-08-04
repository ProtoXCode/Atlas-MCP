import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from server.mcp_instances import mcp
import server.agents.scanner_tool as scanner
import server.agents.ollama_agent as ollama
from server.agents.tools import router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("[+] Starting MCP Server...")
    loop = asyncio.get_event_loop()
    loop.create_task(mcp.run_stdio_async())
    yield
    print("[/] Stopping MCP Server...")


app = FastAPI(title="Atlas MCP Backend", lifespan=lifespan)
app.include_router(router)


@app.get('/')
async def root():
    return {'status': 'Atlas MCP backend is live.'}


@app.get('/_scan')  # TODO: Does not work. Problem with client_session()
async def scan_devices():
    try:
        result = await scanner.scan_network()
        return {'result': result}
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)


@app.get('/scan')
async def scan_devices():
    try:
        result = await ollama.scan_network()
        return {"result": result}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
