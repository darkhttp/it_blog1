from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import MyRegistrationForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'registration.html', context)
