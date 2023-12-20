from .models import *
from django.forms import ModelForm


class NoteForm(ModelForm):
    class Meta:

        model = Note
        fields = '__all__'
