from django.conf import settings
from django.http import HttpResponseForbidden

ALLOWED_FRONTEND = settings.list("ALLOWED_FRONTEND")

class DomainAndAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path = request.path
        origin = request.META.get('HTTP_ORIGIN')
        api_key = request.headers.get('X-API-KEY')

        if path.startswith('/api/v1/'):
            if origin not in ALLOWED_FRONTEND:
                return HttpResponseForbidden("Domain blocked")

            if api_key != settings.FRONTEND_API_KEY:
                return HttpResponseForbidden("Invalid API key")

            return self.get_response(request)

        if path.startswith('/admin/'):
            return self.get_response(request)

        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("Admins only")

        return self.get_response(request)
