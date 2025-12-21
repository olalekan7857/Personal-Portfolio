from django.shortcuts import render, redirect
from .forms import Contact_form
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject=f"New Message from {name}: {subject}",
                message=f"Name: {name}\n Phone_number: {phone_number}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Now save the form to the database
            form.save()

            messages.success(request, "Your message was sent successfully.")
            return redirect('index')
    else:
        form = Contact_form()

    websites = Portfolio.objects.all().order_by('-id')

    context = {
        'form':form,
        'websites':websites,
    }    
    return render(request, 'index.html', context)