import datetime

from rest_framework import mixins, viewsets

from .models import Session, Shot
from .serializers import SessionSerializer, ShotSerializer
from skystats.v1.export.data_source import DataSource
from skystats.v1.export.excel import excel_http_response


class ShotViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer


class SessionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def list(self, request):
        if not request.query_params.get("action"):
            return super().list(request)

        if request.query_params.get("action") == "download":
            session_ids = [
                int(_id) for _id in request.query_params.get("id").split(",")
            ]

            serializer = SessionSerializer(
                Session.objects.filter(id__in=session_ids), many=True
            )

            for row in serializer.data:
                row["clubs_used"] = ", ".join(row["clubs_used"])

            columns = (
                "id",
                "name",
                "timestamp",
                "session_type",
                "clubs_used",
                "shots_count",
            )

            sessions = DataSource(
                name="sessions", columns=columns, data=serializer.data
            )

            shot_serializer = ShotSerializer(
                Shot.objects.filter(session__in=session_ids), many=True
            )

            shot_columns = (
                "session",
                "shot_num",
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
                "club",
            )

            shots = DataSource(
                name="shots", columns=shot_columns, data=shot_serializer.data
            )

            return excel_http_response(
                f"sessions-{datetime.date.today()}.xlsx", sessions, shots
            )
