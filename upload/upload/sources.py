"""
Load the data from different file types.
"""

import csv
from io import StringIO
from typing import List

from werkzeug.datastructures import FileStorage


def df_from_csv(f: FileStorage) -> List[List[str]]:
    """
    Load the data from a csv file.
    """
    data = StringIO(f.read().decode("utf-8"))
    reader = csv.reader(data)
    return [row for row in reader]


def df_from_pdf(f: FileStorage) -> List[List[str]]:
    """
    Load the data from a pdf file.
    """
    pass


FUNCTION_MAPPING = {"csv": df_from_csv, "pdf": df_from_pdf}


def data_from_file(f: FileStorage, file_type: str) -> List[List[str]]:
    """
    Returns the data the file for a given name.
    """
    return FUNCTION_MAPPING[file_type](f)
