from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import cache_control
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
@cache_control(max_age=3600)
def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/tnx/")

    else:
        form = NoteForm()

    return render(request, "home.html", {"form": form})


def tnx(request):
    note = Note.objects.all()
    context = {'note':note}
    return render(request, template_name='tnx.html', context=context)

class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


