from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, cv_detail, generate_pdf, CVViewSet

router = DefaultRouter()
router.register(r"cvs", CVViewSet, basename="cv")

urlpatterns = [
    path("", home, name="home"),
    path("cv/<int:cv_id>/", cv_detail, name="cv_detail"),
    path("cv/<int:cv_id>/download/", generate_pdf, name="cv_download"),
    path("api/", include(router.urls)),
]