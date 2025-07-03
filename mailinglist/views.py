from django.shortcuts import render
from .forms import SubscriberForm


def subscribe(request):
    success = False
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = SubscriberForm()
    return render(request, 'home/index.html', {'form': form, 'success': success})
