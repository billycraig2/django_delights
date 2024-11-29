from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')