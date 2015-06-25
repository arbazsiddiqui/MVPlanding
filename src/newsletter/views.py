from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    title = "WATUP MOFO"
    form = SignUpForm(request.POST or None)
    context = {
        "title" : title,
        "form" : form
    }

    if form.is_valid():
        form.save()
        context ={
            "title" : "Thank you for signing"
        }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        toemail=[email]
        send_mail('Thanks for contacting',
              message,
              settings.EMAIL_HOST_USER,
              toemail,
              fail_silently=False

        )
    context={
        "form" :form
    }
    return render(request, "contact.html", context)

def about(request):
    return render(request, "about.html", {})