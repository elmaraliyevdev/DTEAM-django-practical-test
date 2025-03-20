from django.urls import path
from .views import home, cv_detail, generate_pdf

urlpatterns = [
    path("", home, name="home"),
    path("cv/<int:cv_id>/", cv_detail, name="cv_detail"),
    path("cv/<int:cv_id>/download/", generate_pdf, name="cv_download"),
]