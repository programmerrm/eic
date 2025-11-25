from django.http import JsonResponse

def healthz(request):
    return JsonResponse({"status": "Healthz ok!"}, status=200)
