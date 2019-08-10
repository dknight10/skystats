import pytest
import requests


@pytest.fixture(scope="session")
def auth_headers():
    creds = {
        "client_id": "jBotZ1aP78z5fO359XFevbwLuI6AE0of",
        "client_secret": "ODXLFEC0VcFQRiIY203aYIrX1Va_kMmS8QX4402IhQUVasc8_KtN9WLHgjFhuPpQ",
        "audience": "https://skytrakstats.com/api",
        "grant_type": "client_credentials",
    }

    res = requests.post("https://dk-test.auth0.com/oauth/token", json=creds)

    return {"HTTP_AUTHORIZATION": f"Bearer {res.json()['access_token']}"}
