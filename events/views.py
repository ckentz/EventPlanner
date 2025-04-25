from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, RSVP
from .forms import EventForm

# Event CRUD Views

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


@login_required
def event_list(request):
    events = Event.objects.filter(organizer=request.user).order_by('date')
    return render(request, 'events/event_list.html', {'events': events})



@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})


# RSVP + Event Detail

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_attending = RSVP.objects.filter(user=request.user, event=event).exists()
    attendees = RSVP.objects.filter(event=event)

    if request.method == 'POST':
        if is_attending:
            RSVP.objects.filter(user=request.user, event=event).delete()
            messages.warning(request, "You have canceled your RSVP.")
        else:
            RSVP.objects.create(user=request.user, event=event)
            messages.success(request, "You have RSVP'd to this event.")
        return redirect('event_detail', event_id=event.id)

    return render(request, 'events/event_detail.html', {
        'event': event,
        'attendees': attendees,
        'is_attending': is_attending,
    })

# Public Browsing

@login_required
def browse_events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/browse_events.html', {'events': events})
