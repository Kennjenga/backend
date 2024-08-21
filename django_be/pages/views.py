from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request, *args, **kwargs):
    print(request.user)
    return render(request,'home.html',{})

def aboutpage(request):
    return render(request, 'about.html', {})

def display(request):
    my_context = {
        "tex": "This is some text",
        "num": 5856,
        "my_lis": [23, 434,545,566],
    }
    return render(request, 'display.html',my_context)
