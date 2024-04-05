from django.shortcuts import render

# Create your views here.
from .models import Film

def filmlist(request):
    items = Film.objects.all()
    return render(request, 'listfilm.html', {'items': items})
def filmlist23(request):
    items = Film.objects.filter(name='abc')
    return render(request, 'listfilm.html', {'items': items})