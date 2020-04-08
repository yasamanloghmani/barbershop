from django.shortcuts import render
from .models import Barber
# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def barbers_index(request):
    barbers = Barber.objects.all()
    return render(request, 'barbers/index.html', {'barbers' : barbers})

def barbers_detail(request, barber_id):
    barber = Barber.objects.get(id=barber_id)
    return render(request, 'barbers/detail.html', {'barber' : barber})