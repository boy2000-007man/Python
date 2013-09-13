from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
index = """<title>Calc</title>
    <form method="POST" ACTION="/calc">
    <input type="text" name="number" value="%s">
    <table border="0">
    <tr>
        <td><input type="submit" name="n" value="0"></td>
        <td><input type="submit" name="n" value="1"></td>
        <td><input type="submit" name="n" value="2"></td>
        <td><input type="submit" name="n" value="3"></td>
        <td><input type="submit" name="n" value="4"></td>
    </tr>
    <tr>
        <td><input type="submit" name="n" value="5"></td>
        <td><input type="submit" name="n" value="6"></td>
        <td><input type="submit" name="n" value="7"></td>
        <td><input type="submit" name="n" value="8"></td>
        <td><input type="submit" name="n" value="9"></td>
    </tr>
    <tr>
        <td><input type="submit" name="o" value="+"></td>
        <td><input type="submit" name="o" value="-"></td>
        <td><input type="submit" name="o" value="*"></td>
        <td><input type="submit" name="o" value="/"></td>
        <td><input type="submit" name="e" value="="></td>
    </tr>
    """
@csrf_exempt
def calc(request):
    if request.POST.has_key('n'):
        if str(request.POST['number']) == "0":
            return HttpResponse(index % str(request.POST['n']))
        return HttpResponse(index % (str(request.POST['number']) + str(request.POST['n'])))
    elif request.POST.has_key('o'):
        if not request.POST['number']:
            return HttpResponse(index % "0")
        return HttpResponse(index % (str(request.POST['number']) + str(request.POST['o'])))
    elif request.POST.has_key('e'):
        if not request.POST['number']:
            return HttpResponse(index % "0")
        return HttpResponse(index % eval(str(request.POST['number'])))
    return HttpResponse(index % "0")
