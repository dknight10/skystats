from rest_framework import mixins, viewsets

from .models import Shot
from .serializers import ShotSerializer


class CreateManyModelMixin(mixins.CreateModelMixin):
    def get_serializer(self, *args, **kwargs):
        kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)


class ShotViewSet(
    CreateManyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer
