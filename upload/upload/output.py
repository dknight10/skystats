"""
Collection of different output sources for the parsed data
"""

import csv
from pprint import pprint
from typing import Any, List

import requests

from upload.exceptions import ConfigurationException


class Output:
    """
    Base class that all output classes should inherit from
    """

    def __init__(self, location: str, data: List[Any]) -> None:
        self.location = location
        self.data = data

    def send(self) -> None:
        raise NotImplementedError


class ConsoleOutput(Output):
    """
    Write the data to the console
    """

    def send(self) -> None:
        pprint(self.data)


class FileOutput(Output):
    """
    Write the data to a csv file
    """

    def send(self) -> None:
        if not self.data:
            return
        with open(self.location, "w") as f:
            if isinstance(self.data[0], list):
                writer = csv.writer(f)
            elif isinstance(self.data[0], dict):
                # Assumes fields will remain constant for all rows
                writer = csv.DictWriter(  # type: ignore
                    f, fieldnames=list(self.data[0].keys())
                )
                writer.writeheader()  # type: ignore

            for line in self.data:
                writer.writerow(line)


class ApiOutput(Output):
    """
    Send the data as json to another API endpoint
    """

    def send(self) -> None:
        requests.post(self.location, json=self.data)


OUTPUT_MAPPING = {"console": ConsoleOutput, "file": FileOutput, "api": ApiOutput}


def handle_output(output_type: str, location: str, data: List[Any]) -> None:
    """
    Instantiates and calls send for the given output type
    """
    try:
        output_class = OUTPUT_MAPPING[output_type]
    except KeyError:
        raise ConfigurationException(f"{output_type} is not a supported output type")
    output = output_class(location, data)
    output.send()
