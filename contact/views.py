from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email sent successfully!')
            return redirect(reverse('contact'))
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
