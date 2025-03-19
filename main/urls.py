from django.urls import path
from .views import home, cv_detail

urlpatterns = [
    path("", home, name="home"),
    path("cv/<int:cv_id>/", cv_detail, name="cv_detail"),
]