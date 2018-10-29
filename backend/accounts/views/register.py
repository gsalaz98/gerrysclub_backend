from django.contrib.auth.forms import UserCreationForm
from django.http import Http404 
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        ctx = {
            'registration_form': form,
        }
        return render(request, 'register.html', context=ctx)

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        return Http404()

def registration_successful(request):
    return render(request, 'registration_successful.html')
