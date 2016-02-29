from django.shortcuts import render
from django.http import HttpResponse
from register.models import User
from register.forms import UserForm
from django.core.mail import send_mail


def index(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'register/successPage.html')

        else:
            print form.errors
    else:
        form = UserForm()

    return render(request, 'register/register.html', {'form': form})
