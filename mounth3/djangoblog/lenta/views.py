from django.http import HttpResponse

# Create your views here.

def show_lenta(request):
    return HttpResponse(f'Hello World | method - {request.method} path - ({request.path})')

def add_like(request):
    return HttpResponse(f'Added like | method - {request.method} path - ({request.path})')

def add_comment(request):
    return HttpResponse(f'Added comment | method - {request.method} path - ({request.path})')

def add_post(request):
    return HttpResponse(f'Added post | method - {request.method} path - ({request.path})')

# def add_answer(request):
#     return HttpResponse(str(input('Which method did you use to find our resource?: ')))