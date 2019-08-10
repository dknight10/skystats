import os

import requests


def get_token():
    creds = {
        "client_id": os.environ["AUTH0_CLIENT_ID"],
        "client_secret": os.environ["AUTH0_CLIENT_SECRET"],
        "audience": os.environ["AUTH0_AUDIENCE"],
        "grant_type": os.environ["AUTH0_GRANT_TYPE"],
    }

    res = requests.post(os.environ["AUTH0_URL"], json=creds)

    return res.json()["access_token"]
