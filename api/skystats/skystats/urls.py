from django.urls import include, path

urlpatterns = [path("v1/", include("skystats.v1.urls"))]
