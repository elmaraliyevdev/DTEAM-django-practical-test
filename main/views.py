try:
    import weasyprint
except OSError:
    # Create a mock weasyprint module for development
    class MockWeasyPrint:
        class HTML:
            def __init__(self, string=None, base_url=None):
                self.string = string
                self.base_url = base_url
            
            def write_pdf(self, target=None):
                # Just return some dummy PDF content for testing
                if target:
                    with open(target, 'wb') as f:
                        f.write(b'%PDF-1.4\nMock PDF Content')
                return b'%PDF-1.4\nMock PDF Content'
    
    weasyprint = MockWeasyPrint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import CV, RequestLog
from .serializers import CVSerializer
from rest_framework import viewsets

def home(request):
    cvs = CV.objects.all()
    return render(request, "main/home.html", {"cvs": cvs})


def cv_detail(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    return render(request, "main/cv_detail.html", {"cv": cv})


def generate_pdf(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    html_content = render_to_string("main/cv_pdf_template.html", {"cv": cv})
    pdf_file = weasyprint.HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{cv.firstname}_{cv.lastname}.pdf"'
    return response

def settings_view(request):
    """Displays selected Django settings in a template."""
    return render(request, "main/settings.html")


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


def logs(request):
    logs = RequestLog.objects.order_by("-timestamp")[:10]  # Get the last 10 requests
    return render(request, "main/logs.html", {"logs": logs})