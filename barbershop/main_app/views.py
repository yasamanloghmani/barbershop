from django.shortcuts import render
from .models import Barber
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def barbers_index(request):
    barbers = Barber.objects.all()
    return render(request, 'barbers/index.html', {'barbers' : barbers})

def barbers_detail(request, barber_id):
    barber = Barber.objects.get(id=barber_id)
    return render(request, 'barbers/detail.html', {'barber' : barber})

class BarberCreate(CreateView):
  model = Barber
  fields = '__all__'


class BarberUpdate(UpdateView):
  model = Barber
  fields = ['age', 'experience', 'description']

class BarberDelete(DeleteView):
  model = Barber
  success_url = '/barbers/'

  