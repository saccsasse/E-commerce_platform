from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import CreateUserForm

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            #Email verification logic
            subject = 'Activate your account.'
            message = ''
            return redirect('index')
    return render(request, 'users/register.html', {'form': form})


def email_verification(request):
    pass

def email_verification_sent(request):
    pass

def email_verification_success(request):
    pass

def email_verification_failed(request):
    pass