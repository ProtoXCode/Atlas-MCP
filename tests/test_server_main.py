import pytest
from httpx import ASGITransport, AsyncClient

from server.main import app

transport = ASGITransport(app=app)


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert "status" in response.json()

# Make sure Ollama is running
@pytest.mark.asyncio
async def test_scan():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/scan")
        assert response.status_code == 200
        assert "result" in response.json()
