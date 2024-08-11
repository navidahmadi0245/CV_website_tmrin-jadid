from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    return render(request,'website/contact.html')
def test_view(request):
    context={'title': 'salam', 'content': '://'}
    return render(request,'website/test.html',context)
