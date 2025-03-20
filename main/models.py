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


class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    http_method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_string = models.TextField(blank=True, null=True)
    remote_ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.http_method} {self.path} at {self.timestamp}"