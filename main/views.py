from django.shortcuts import render, get_object_or_404
from .models import CV

def home(request):
    cvs = CV.objects.all()
    return render(request, "main/home.html", {"cvs": cvs})


def cv_detail(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    return render(request, "main/cv_detail.html", {"cv": cv})