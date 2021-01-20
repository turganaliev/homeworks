from django.http import HttpResponse

# Create your views here.

def show_lenta(request):
    return HttpResponse('Hello World')

def add_like(request):
    return HttpResponse('Added like')

def add_comment(request):
    return HttpResponse('Added comment')

def add_post(request):
    return HttpResponse('Added post')

def add_answer(request):
    return HttpResponse(str(input('Which method did you use to find our resource?: ')))