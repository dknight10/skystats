"""
Classify the data source by the file name.
"""

import re
from dataclasses import dataclass

from upload.exceptions import InvalidFileException

FILE_RE = r"Export_([a-zA-Z]+)_.*?\.([a-z]+)"

TYPES = {"SA": "swing analysis", "ShotsHistory": "driving range"}
VALID_EXTENSIONS = ["csv", "pdf"]


@dataclass
class DataType:
    session_type: str
    file_type: str


def classify_filename(name: str) -> DataType:
    """
    Parse the data type and file type info based on the file name.
    """
    match = re.match(FILE_RE, name)

    if not match:
        raise InvalidFileException(f"{name} is not a valid file")

    try:
        session_type, file_type = match.group(1), match.group(2)
    except (IndexError, AttributeError):
        raise InvalidFileException(f"{name} is not a valid file")

    try:
        session_type = TYPES[session_type]
    except KeyError:
        raise InvalidFileException(f"{session_type} is not a valid session type")

    if file_type not in VALID_EXTENSIONS:
        raise InvalidFileException(f"{file_type} is not a valid extension")

    return DataType(session_type, file_type)
