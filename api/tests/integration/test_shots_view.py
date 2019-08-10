import datetime
from decimal import Decimal

import pytest
import pytz
from django.forms.models import model_to_dict

from skystats.v1.shots.models import Session, Shot


sample = {
    "name": "Donny Knight",
    "timestamp": "2019-06-29T15:29",
    "session_type": "practice",
    "user": "donny@test.com",
    "shots": [
        {
            "id": 1,
            "shot_num": 1,
            "hand": "R",
            "ball_speed": "33",
            "launch_angle": "40.8",
            "back_spin": "1997",
            "side_spin": "258",
            "side_angle": "0.0",
            "offline_distance": "0",
            "carry": "22",
            "roll": "1",
            "total": "23",
            "hang_time": "2.1",
            "descent_angle": "43.3",
            "peak_height": "5",
            "club_speed": "25",
            "pti": "1.30",
            "club": "undefined",
        },
        {
            "id": 2,
            "shot_num": "2",
            "hand": "R",
            "ball_speed": "32",
            "launch_angle": "24.8",
            "back_spin": "2560",
            "side_spin": "1040",
            "side_angle": "2.7",
            "offline_distance": "2",
            "carry": "18",
            "roll": "2",
            "total": "20",
            "hang_time": "1.4",
            "descent_angle": "26.2",
            "peak_height": "2",
            "club_speed": "28",
            "pti": "1.17",
            "club": "undefined",
        },
        {
            "id": 3,
            "shot_num": "3",
            "hand": "R",
            "ball_speed": "32",
            "launch_angle": "39.2",
            "back_spin": "2051",
            "side_spin": "416",
            "side_angle": "-6.4",
            "offline_distance": "-2",
            "carry": "21",
            "roll": "1",
            "total": "22",
            "hang_time": "1.9",
            "descent_angle": "41.7",
            "peak_height": "4",
            "club_speed": "25",
            "pti": "1.28",
            "club": "undefined",
        },
    ],
}


@pytest.mark.django_db
def test_shots_view_creates_shots_and_session(client, auth_headers, mocker):
    expected_shots = [
        {
            "session": 1,
            "id": 1,
            "shot_num": 1,
            "hand": "R",
            "ball_speed": 33,
            "launch_angle": Decimal("40.8"),
            "back_spin": 1997,
            "side_spin": 258,
            "side_angle": Decimal("0.0"),
            "offline_distance": 0,
            "carry": 22,
            "roll": 1,
            "total": 23,
            "hang_time": Decimal("2.1"),
            "descent_angle": Decimal("43.3"),
            "peak_height": 5,
            "club_speed": 25,
            "pti": Decimal("1.30"),
            "club": "undefined",
        },
        {
            "session": 1,
            "id": 2,
            "shot_num": 2,
            "hand": "R",
            "ball_speed": 32,
            "launch_angle": Decimal("24.8"),
            "back_spin": 2560,
            "side_spin": 1040,
            "side_angle": Decimal("2.7"),
            "offline_distance": 2,
            "carry": 18,
            "roll": 2,
            "total": 20,
            "hang_time": Decimal("1.4"),
            "descent_angle": Decimal("26.2"),
            "peak_height": 2,
            "club_speed": 28,
            "pti": Decimal("1.17"),
            "club": "undefined",
        },
        {
            "session": 1,
            "id": 3,
            "shot_num": 3,
            "hand": "R",
            "ball_speed": 32,
            "launch_angle": Decimal("39.2"),
            "back_spin": 2051,
            "side_spin": 416,
            "side_angle": Decimal("-6.4"),
            "offline_distance": -2,
            "carry": 21,
            "roll": 1,
            "total": 22,
            "hang_time": Decimal("1.9"),
            "descent_angle": Decimal("41.7"),
            "peak_height": 4,
            "club_speed": 25,
            "pti": Decimal("1.28"),
            "club": "undefined",
        },
    ]
    mocker.patch(
        "skystats.shared.auth.get_email_from_user_info", return_value="donny@test.com"
    )
    client.post(
        "/v1/sessions/", sample, content_type="application/json", **auth_headers
    )
    session = Session.objects.get(id=1)
    assert session.name == "Donny Knight"
    assert session.timestamp == datetime.datetime(2019, 6, 29, 15, 29, tzinfo=pytz.UTC)
    assert session.session_type == "practice"
    assert session.user == "donny@test.com"

    for n, shot in enumerate(Shot.objects.all()):
        assert model_to_dict(shot) == expected_shots[n]


@pytest.mark.django_db
def test_session_unique_contraints(client, auth_headers, mocker):
    mocker.patch(
        "skystats.shared.auth.get_email_from_user_info", return_value="donny@test.com"
    )
    test_obj = {
        "name": "Test",
        "timestamp": "2019-06-29T15:29",
        "session_type": "practice",
        "shots": [],
        "user": "donny@test.com",
    }
    client.post(
        "/v1/sessions/", test_obj, content_type="application/json", **auth_headers
    )
    client.post(
        "/v1/sessions/", test_obj, content_type="application/json", **auth_headers
    )
    assert len(Session.objects.all()) == 1
