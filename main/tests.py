from django.test import TestCase
from django.urls import reverse
from .models import CV

class CVTestCase(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="Jane",
            lastname="Doe",
            skills="Django, Python",
            projects="Portfolio website",
            bio="Software developer",
            contacts="Email: jane@example.com"
        )

    def test_cv_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")

    def test_cv_detail_view(self):
        cv = CV.objects.first()
        response = self.client.get(f"/cv/{cv.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django, Python")

    def test_pdf_download(self):
        response = self.client.get(reverse("cv_download", args=[self.cv.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")