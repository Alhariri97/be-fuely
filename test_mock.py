import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello":"Tea(m)418", "Am_I_In_The_Right_Place":"Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}
    assert response.json()["hello"] == "Tea(m)48" 