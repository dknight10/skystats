"""
Extracts the cleaned data from a given data file
"""

from typing import Dict, List

from werkzeug.datastructures import FileStorage

from upload.classify import classify_filename
from upload.parsing import json_from_raw
from upload.sources import data_from_file


def extract_data(f: FileStorage) -> List[Dict[str, str]]:
    """
    Main controller for extracting the data from the
    Skytrak data file.

    1. Determines the data type based on the file name
    2. Grabs the data from the given file type
    3. Formats the data and returns as json
    """
    data_type = classify_filename(f.filename)
    data = data_from_file(f, data_type.file_type)
    return json_from_raw(data, data_type.session_type)
