from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import *

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@mailtrap.io",
                ["django@hecktor.net"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})
