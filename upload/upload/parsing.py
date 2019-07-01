"""
Parse the raw data into a usable format.
"""

import datetime
from collections import defaultdict
from typing import Any, Dict, List, Optional

from upload.exceptions import ParsingException


SKYTRAK_TIMESTAMP_FORMAT = "%m/%d/%Y %I:%M %p"


class SessionInfo:
    """
    Metadata included in the Skytrak data files.
    """

    def __init__(self) -> None:
        self.name: Optional[str] = None
        self.timestamp: Optional[datetime.datetime] = None
        self.type_: Optional[str] = None
        self.notes: Dict[str, str] = {}

    def json(self) -> Dict[str, Any]:
        if not all([self.name, self.type_, self.timestamp]):
            raise ParsingException("name, timestamp, or type missing from session info")
        return {
            "name": self.name,
            "timestamp": self.timestamp.isoformat(timespec="minutes"),  # type: ignore
            "type": self.type_,
            "notes": self.notes,
        }


class Parser:
    pass


class RangeDataParser(Parser):
    """
    Parses data of the raw shot data tables.

    This is the format of the data for the driving range, skills assessment, and
    game improvement when exporting the data from the history tab.
    """

    COLUMNS = [
        "SHOT",
        "HAND",
        "BALL",
        "LAUNCH",
        "BACK",
        "SIDE",
        "SIDE",
        "OFFLINE",
        "CARRY",
        "ROLL",
        "TOTAL",
        "FLIGHT",
        "DSCNT",
        "HEIGHT",
        "CLUB",
        "PTI",
    ]
    NAMES = [
        "shot",
        "hand",
        "ball_speed",
        "launch_angle",
        "back_spin",
        "side_spin",
        "side_angle",
        "offline_distance",
        "carry",
        "roll",
        "total",
        "hang_time",
        "descent_angle",
        "peak_height",
        "club_speed",
        "pti",
    ]

    def __init__(self, data: List[List[str]]) -> None:
        self.raw_data = data
        self.session_info = SessionInfo()

    def extract_name(self) -> None:
        """
        Exracts the username and sets it's value in SessionSettings.
        """
        try:
            field = self.raw_data[2][0]
        except IndexError:
            raise ParsingException(
                "Could not extract name from data, name field not present"
            )

        try:
            name = field.split(":")[1].strip()
        except IndexError:
            raise ParsingException(
                "Could not extract name from data, incorrect field format"
            )

        self.session_info.name = name.title()

    def extract_type(self) -> None:
        """
        Exracts the session type and sets it's value in SessionSettings.
        """
        try:
            field = self.raw_data[1][0]
        except IndexError:
            raise ParsingException(
                "Could not extract type from data, type field not present"
            )

        try:
            type_ = field.split(":")[0].strip()
        except IndexError:
            raise ParsingException(
                "Could not extract type from data, incorrect field format"
            )

        self.session_info.type_ = type_.lower()

    def extract_timestamp(self) -> None:
        """
        Exracts the timestamp of the session and sets it's value in SessionSettings.
        """
        try:
            field = self.raw_data[1][0]
        except IndexError:
            raise ParsingException(
                "Could not timestamp name from data, timestamp field not present"
            )

        try:
            timestamp = field.split(":", 1)[1].strip()
        except IndexError:
            raise ParsingException(
                "Could not extract timestamp from data, incorrect field format"
            )

        self.session_info.timestamp = datetime.datetime.strptime(
            timestamp, SKYTRAK_TIMESTAMP_FORMAT
        )

    def extract_notes(self) -> None:
        """
        Exracts the session notes that are included in the export field
        and sets it's value in SessionSettings.
        """
        pass

    def verify_columns(self) -> None:
        """
        Verifies that the columns of the data are expected.
        """
        try:
            row = self.raw_data[4]
        except IndexError:
            raise ParsingException(
                "Could not extract columns from data, column row not present"
            )

        if row != self.COLUMNS:
            raise ParsingException("Invalid columns for Range Data")

    def data_by_club(self) -> Dict[str, List[List[str]]]:
        """
        Gathers the data by club from the raw data and combines them
        for the given club.
        """
        data: Dict[str, List[List[str]]] = defaultdict(list)
        started = False
        club = ""
        for row in self.raw_data:
            if not started:
                if row[0] == "#":
                    started = True
                continue

            if not row[0] or row[0] == "AVG":
                continue

            if row[0] == "NOTES":
                break

            try:
                int(row[0])
            except ValueError:
                data_row = False
            else:
                data_row = True

            if data_row:
                data[club].append(row)
            else:
                club = row[0].split("#")[0].strip().lower()

        return data

    def data_rows(self) -> List[Dict[str, str]]:
        """
        Transforms the data by club into a large list of dicts.
        """
        data: List[Dict[str, str]] = []
        shot_num = 1
        for club, rows in self.data_by_club().items():
            for row in rows:
                row_dict = {}
                for n, item in enumerate(row):
                    row_dict[self.NAMES[n]] = item
                    row_dict["club"] = club
                    row_dict["shot"] = str(shot_num)
                data.append(row_dict)
                shot_num += 1

        return data

    def json(self) -> List[Dict[str, str]]:
        """
        Calls all verification and extraction steps then adds the metadata
        to each row.
        """
        self.verify_columns()
        self.extract_name()
        self.extract_type()
        self.extract_timestamp()
        self.extract_notes()
        meta = self.session_info.json()
        data = self.data_rows()
        for row in data:
            row.update(meta)
        return data


PARSER_MAPPING = {"driving range": RangeDataParser}


def json_from_raw(data: List[List[str]], session_type: str) -> List[Dict[str, str]]:
    """
    Returns formatted json data for the given raw data type.
    """
    parser = PARSER_MAPPING[session_type](data)
    return parser.json()
