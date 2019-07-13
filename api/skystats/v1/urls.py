from django.urls import include, path

urlpatterns = [path(r"v1/", include("skystats.v1.shots.urls"))]
