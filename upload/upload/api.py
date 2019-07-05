"""
API endpoint to process Skytrak data files and send it
to another endpoint.
"""

import os
from pathlib import Path

from flask import Flask, jsonify, request

from upload.extract import extract_data
from upload.output import handle_output

app = Flask(__name__)
# Set max upload size to 8MB
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

ALLOWED_EXTENSIONS = [".csv", ".pdf"]

OUTPUT_TYPE = os.environ.get("OUTPUT_TYPE")
OUTPUT_LOCATION = os.environ.get("OUTPUT_LOCATION")


def allowed_file(name: str) -> bool:
    """
    Verifies the incoming file by checking the extension
    """
    p = Path(name)
    if p.suffix and p.suffix.lower() in ALLOWED_EXTENSIONS:
        return True
    return False


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
        f = request.files["attachment-1"]
    except KeyError:
        return "Must pass pdf or csv as attachment", 400

    if not allowed_file(f.filename):
        return "Must pass pdf or csv as attachment", 400

    data = extract_data(f)
    if OUTPUT_TYPE:
        handle_output(OUTPUT_TYPE, OUTPUT_LOCATION, data)

    return jsonify(data), 200
