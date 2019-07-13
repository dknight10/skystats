from django.urls import include, path

urlpatterns = [path(r"", include("skystats.v1.urls"))]
