from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request, 'demo.html')

def about_view(request):
    return HttpResponse("About Us")