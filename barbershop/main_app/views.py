from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
class Barber:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

barbers = [
  Barber('Lolo', 'tabby', 'foul little demon', 3),
  Barber('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Barber('Raven', 'black tripod', '3 legged cat', 4)
]
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def barbers_index(request):
    return render(request, 'barbers/index.html', {'barbers' : barbers})