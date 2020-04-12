from django.forms import ModelForm
from .models import Schedule

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time', 'skill']
        