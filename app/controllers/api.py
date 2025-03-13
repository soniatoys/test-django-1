from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"message": "API de App 1 funcionando"})
