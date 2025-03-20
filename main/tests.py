from django.test import TestCase
from django.urls import reverse
from rest_framework import status
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
        self.api_url = reverse("cv-list")
    
    def test_get_cv_list(self):
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)

    def test_create_cv(self):
        data = {
            "firstname": "Alice",
            "lastname": "Smith",
            "skills": "React, JavaScript",
            "projects": "E-commerce website",
            "bio": "Frontend developer",
            "contacts": "Email: alice@example.com"
        }
        response = self.client.post(self.api_url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_cv(self):
        response = self.client.get(reverse("cv-detail", args=[self.cv.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["firstname"], "Jane")

    def test_update_cv(self):
        data = {"firstname": "Jane Updated"}
        response = self.client.patch(reverse("cv-detail", args=[self.cv.id]), data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cv.refresh_from_db()
        self.assertEqual(self.cv.firstname, "Jane Updated")

    def test_delete_cv(self):
        response = self.client.delete(reverse("cv-detail", args=[self.cv.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CV.objects.filter(id=self.cv.id).exists())

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