from .models import RequestLog
from django.utils.timezone import now

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract relevant request data
        user = request.user.username if request.user.is_authenticated else "Anonymous"
        remote_ip = request.META.get("REMOTE_ADDR")
        query_string = request.META.get("QUERY_STRING", "")

        # Save request log to the database
        RequestLog.objects.create(
            timestamp=now(),
            http_method=request.method,
            path=request.path,
            query_string=query_string,
            remote_ip=remote_ip,
            user=user
        )

        return self.get_response(request)