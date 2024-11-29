from django.shortcuts import render
from .models import InventoryItem

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')