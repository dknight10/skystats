from django.urls import include, path

urlpatterns = [path("shots/", include("v1.shots.urls"))]
