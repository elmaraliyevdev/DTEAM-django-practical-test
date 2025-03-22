from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, cv_detail, generate_pdf, CVViewSet, logs, settings_view, send_cv_email, career_advice

router = DefaultRouter()
router.register(r"cvs", CVViewSet, basename="cv")

urlpatterns = [
    path("", home, name="home"),
    path("cv/<int:cv_id>/", cv_detail, name="cv_detail"),
    path("cv/<int:cv_id>/download/", generate_pdf, name="cv_download"),
    path("cv/<int:cv_id>/send-email/", send_cv_email, name="send_cv_email"),
    path("settings/", settings_view, name="settings"),
    path("logs/", logs, name="logs"),
    path("api/", include(router.urls)),
    path("api/cv/<int:cv_id>/career-advice/", career_advice, name="career_advice"),
]