from django.http import HttpResponse

def index(request):
    return HttpResponse('pollsのトップページ')

# プチ演習
def test(request):
    return HttpResponse('testページ')