from django.shortcuts import render
from .models import Event
from .forms import EventForm

def make(request):
    if request.method == "POST":
        form = EventForm(request.POST)
    else:
        form = EventForm()
    return render(request, 'makeevent/index.html', {
        'form': form
    })
