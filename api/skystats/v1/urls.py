from django.urls import include, path

urlpatterns = [path("shots/", include("skystats.v1.shots.urls"))]
