# Create your views here.
from django.shortcuts import render

def home(request):
    # This function takes the web request and returns our HTML template
    return render(request, 'hello.html')
