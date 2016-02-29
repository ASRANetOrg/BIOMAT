from django.shortcuts import render
from django.http import HttpResponse
from uploadAbstract.models import SubmittedAbstract
from uploadAbstract.forms import UserForm


def index(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'uploadAbstract/successPage.html')

        else:
            print form.errors
    else:
        form = UserForm()

    return render(request, 'uploadAbstract/uploadAbstract.html', {'form': form})
