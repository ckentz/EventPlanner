from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')  # we'll make this view next
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})
