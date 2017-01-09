from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'registration/registration.html',{})

@login_required()
def profile(request):
    return render(request, 'registration/profile.html',{})


def exchange(request):
    return render(request, 'forms/formExchange.html', {})


def institution(request):
    return render(request, 'forms/addInstitution.html', {})


def funded(request):
    return render(request, 'forms/formFunded.html', {})
