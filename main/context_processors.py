from django.conf import settings

def settings_context(request):
    """Injects Django settings into templates."""
    return {"settings": settings}