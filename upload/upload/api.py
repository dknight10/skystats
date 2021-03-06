"""
API endpoint to process Skytrak data files and send it
to another endpoint.
"""
import logging
import os
import re
from pathlib import Path

import requests
from flask import Flask, jsonify, request

from upload.auth import get_token
from upload.extract import extract_data

# TODO add json logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)-8s\t%(filename)-14s\t%(message)s",
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
# Set max upload size to 8MB
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

ALLOWED_EXTENSIONS = [".csv", ".pdf"]

API_ENDPOINT = os.environ["API_ENDPOINT"]


def allowed_file(name: str) -> bool:
    """
    Verifies the incoming file by checking the extension
    """
    p = Path(name)
    if p.suffix and p.suffix.lower() in ALLOWED_EXTENSIONS:
        return True
    return False


def extract_email(s: str) -> str:
    match = re.match(r".+<(.+)>", s)
    if not match:
        raise ValueError("Could not extract email address")
    return match.group(1)


@app.route("/upload", methods=["POST"])
def upload_files():
    """
    Receives the raw data as an attachment on an email from
    the Skytrak application and uploads to a given endpoint.

    Steps:
      1. Grabs attachment from the files attribute of the request object
      2. Extracts and formats the given data
      3. Optionally sends the data to an output source
      4. Returns the processed data as json
    """
    try:
        sender = extract_email(request.form["From"])
    except (TypeError, KeyError):
        logger.warning("Could not get sender from request")
        return "Sender must be provided", 400
    except ValueError:
        logger.warning("Error extracting email address")
        return "Could not extract email address", 400

    try:
        f = request.files["attachment-1"]
    except KeyError:
        logger.warning("Request made without needed attachment")
        return "Must pass pdf or csv as attachment", 400

    if not allowed_file(f.filename):
        logger.warning(f"File {f.filename} not allowed")
        return "Must pass pdf or csv as attachment", 400

    data = extract_data(f)
    data["user"] = sender

    logger.info("Data extracted, sending to API")

    res = requests.post(
        API_ENDPOINT, json=data, headers={"Authorization": f"Bearer {get_token()}"}
    )
    if res.status_code == 201:
        logger.info("Successfully posted data to API")
        return jsonify(res.json()), 201
    elif res.status_code == 400:
        logger.warning("Data received contained errors")
        return jsonify(res.json()), 400
    else:
        logger.info(f"Bad status from API {res.status_code}")
        return res.content, res.status_code
