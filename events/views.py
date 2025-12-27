from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participant


def home(request):
    return render(request, 'events/home.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        Participant.objects.create(
            event=event,
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('success')

    return render(request, 'events/register_event.html', {'event': event})


def success(request):
    return render(request, 'events/success.html')
