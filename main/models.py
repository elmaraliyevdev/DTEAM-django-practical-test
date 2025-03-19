from django.db import models

class CV(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    skills = models.TextField()
    projects = models.TextField()
    bio = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
