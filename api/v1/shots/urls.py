from django.urls import include, path
from rest_framework import routers

from .views import ShotViewSet

router = routers.DefaultRouter()
router.register("", ShotViewSet)

urlpatterns = [path("", include(router.urls))]
