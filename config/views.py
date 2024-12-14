from django.http import JsonResponse

def api_only_view(request):
    """
    Страница-заглушка для информирования, что ресурс только для API.
    """
    return JsonResponse({"detail": "This resource is intended only for API."})