from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import weasyprint
from .models import CV

@shared_task
def send_cv_pdf(email, cv_id):
    cv = CV.objects.get(id=cv_id)
    
    # Generate PDF
    html_content = render_to_string("main/cv_pdf_template.html", {"cv": cv})
    pdf_file = weasyprint.HTML(string=html_content).write_pdf()

    # Send Email
    subject = "Your CV PDF"
    message = "Please find your CV attached."
    email_msg = EmailMessage(subject, message, "noreply@example.com", [email])
    email_msg.attach(f"{cv.firstname}_{cv.lastname}.pdf", pdf_file, "application/pdf")
    email_msg.send()