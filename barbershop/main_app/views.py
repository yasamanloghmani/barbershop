from django.shortcuts import render, redirect
from .models import Barber
from .forms import ScheduleForm
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
    schedule_form = ScheduleForm()
    return render(request, 'barbers/detail.html', {'barber' : barber, 'schedule_form' : schedule_form})

class BarberCreate(CreateView):
  model = Barber
  fields = '__all__'


class BarberUpdate(UpdateView):
  model = Barber
  fields = ['age', 'experience', 'description']

class BarberDelete(DeleteView):
  model = Barber
  success_url = '/barbers/'


def add_appointment(request, barber_id):
  form = ScheduleForm(request.POST)
  if form.is_valid():
    new_schedule = form.save(commit=False)
    new_schedule.barber_id = barber_id
    new_schedule.save()
  return redirect('detail', barber_id=barber_id)
  