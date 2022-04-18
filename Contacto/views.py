from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def joinus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = ContactForm()

    return render(request, "Contacto/joinus.html", {"form": form})


