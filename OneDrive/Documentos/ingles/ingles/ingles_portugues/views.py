from django.shortcuts import render, redirect
from .models import Palavras
# Create your views here.
def home(request):
    return render (request, 'home.html')

def palavras(request):
    
    palavras = Palavras.objects.all()[:12]
    return render(request, 'palavras.html', {'palavras':palavras})



