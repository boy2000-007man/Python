from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
index = """<title>Supervisor Search Engine</title>
    <form method="GET" action="/search">
    Keywords:<input type="text" name="keywords">
    <input type="submit"/>
    <form>"""
result = """Search Keyword: %s<br>
    Resutls are: %s.<br>
    <br>
    Click <a href="/search">here</a> to return."""
@csrf_exempt
def search(request):
    if request.GET.has_key("keywords"):
        return HttpResponse(result)
    return HttpResponse(index)
