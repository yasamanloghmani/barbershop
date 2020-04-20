from django.shortcuts import render, redirect
from .models import Barber , Location
from .forms import ScheduleForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
  return redirect('accounts/login/')

@login_required
def barbers_index(request):
    barbers = request.user.barber_set.all()
    return render(request, 'barbers/index.html', {'barbers' : barbers})

@login_required
def barbers_detail(request, barber_id):
    barber = Barber.objects.get(id=barber_id)
    schedule_form = ScheduleForm()
    not_location = Location.objects.exclude(id__in = barber.locations.all().values_list('id'))
    return render(request, 'barbers/detail.html', {'barber' : barber, 'schedule_form' : schedule_form, 'locations' : not_location})

class BarberCreate(LoginRequiredMixin, CreateView):
  model = Barber
  fields = ['name', 'age', 'experience', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class BarberUpdate(LoginRequiredMixin, UpdateView):
  model = Barber
  fields = ['age', 'experience', 'description']

class BarberDelete(LoginRequiredMixin, DeleteView):
  model = Barber
  success_url = '/barbers/'

@login_required
def add_appointment(request, barber_id):
  form = ScheduleForm(request.POST)
  if form.is_valid():
    new_schedule = form.save(commit=False)
    new_schedule.barber_id = barber_id
    new_schedule.save()
  return redirect('detail', barber_id=barber_id)
  
class Locations(LoginRequiredMixin, ListView):
  model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
  model = Location

class LocationCreate(LoginRequiredMixin, CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(LoginRequiredMixin, UpdateView):
  model = Location
  fields = ['name', 'address', 'phone']

class LocationDelete(LoginRequiredMixin, DeleteView):
  model = Location
  success_url = '/locations/'

@login_required
def new_location(request, barber_id, location_id):
  Barber.objects.get(id=barber_id).locations.add(location_id)
  return redirect('detail', barber_id=barber_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)