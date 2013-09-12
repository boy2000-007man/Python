from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
text = """<form method="POST" action="/test/">
    <input type="submit" name="+" value="+">
    <input type="submit" name="-" value="-">
    <input type="text" value="%s">
    <form>"""
@csrf_exempt
def test(request):
    if request.POST.has_key('+'):
        tmp = "++++++++++++"
    else:
        tmp = "-------------------"
    return HttpResponse(text % tmp)
