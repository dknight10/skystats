import datetime

from rest_framework import mixins, viewsets
from rest_framework.exceptions import AuthenticationFailed

from .models import Session, Shot
from .serializers import SessionSerializer, ShotSerializer
from skystats.shared.auth import requires_scope, get_email_from_user_info, AuthError
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
    serializer_class = SessionSerializer

    def get_queryset(self):
        try:
            email = get_email_from_user_info(self.request)
        except AuthError:
            raise AuthenticationFailed("Could not get email for user")

        return Session.objects.filter(user=email)

    @requires_scope("write:sessions")
    def create(self, request):
        return super().create(request)

    @requires_scope("read:sessions")
    def list(self, request):
        if not request.query_params.get("action"):
            return super().list(request)

        if request.query_params.get("action") == "download":
            session_ids = [
                int(_id) for _id in request.query_params.get("id").split(",")
            ]

            # TODO see if a property on the models can be used for display names.
            # Tried using verbose_name, but won't work for the property fields.
            columns = (
                ("id", "session id"),
                "name",
                "timestamp",
                ("session_type", "session type"),
                ("clubs_used_str", "clubs used"),
                ("shots_count", "shots count"),
            )

            sessions = DataSource(
                name="sessions",
                columns=columns,
                data=Session.objects.filter(id__in=session_ids),
            )

            shot_columns = (
                ("session_id", "session id"),
                ("shot_num", "shot number"),
                "hand",
                ("ball_speed", "ball speed"),
                ("launch_angle", "launch angle"),
                ("back_spin", "back spin"),
                ("side_spin", "side spin"),
                ("side_angle", "side angle"),
                ("offline_distance", "offline distance"),
                "carry",
                "roll",
                "total",
                ("hang_time", "hang time"),
                ("descent_angle", "descent angle"),
                ("peak_height", "peak height"),
                ("club_speed", "club speed"),
                "pti",
                "club",
            )

            shots = DataSource(
                name="shots",
                columns=shot_columns,
                data=Shot.objects.filter(session__in=session_ids),
            )

            return excel_http_response(
                f"sessions-{datetime.date.today()}.xlsx", sessions, shots
            )
