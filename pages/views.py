from django.http import HttpResponse



def homePageViev(request):
    return HttpResponse('hello world!')