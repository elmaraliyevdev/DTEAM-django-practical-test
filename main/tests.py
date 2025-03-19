from django.test import TestCase
from .models import CV

class CVTestCase(TestCase):
    def setUp(self):
        CV.objects.create(
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