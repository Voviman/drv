from django.shortcuts import render
from .models import Driver



def home(request):
    driver = Driver.objects.all().order_by('-id')
    return render(request, 'index.html', {'driver': driver})

# Create your views here.
