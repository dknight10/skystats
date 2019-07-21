from django.urls import include, path
from rest_framework import routers

from .views import SessionViewSet, ShotViewSet

shots_router = routers.DefaultRouter()
shots_router.register("", ShotViewSet)

sessions_router = routers.DefaultRouter()
sessions_router.register("", SessionViewSet)

urlpatterns = [
    path("shots/", include(shots_router.urls)),
    path("sessions/", include(sessions_router.urls)),
    path("sessions", include(sessions_router.urls)),
]
