from django import forms
from .models import *

class EventForm(forms.ModelForm):
	
	class Meta:
		model = Events
		fields = ('event_name','event_date','num_participants')