from rest_framework import mixins, viewsets

from .models import Session, Shot
from .serializers import SessionSerializer, ShotSerializer


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
