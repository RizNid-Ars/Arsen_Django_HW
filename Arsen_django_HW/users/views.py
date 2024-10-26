from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', context={'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/register.html', context={'form': form})
        form.cleaned_data.pop('password_confirm')
        User.objects.create(**form.cleaned_data)
        return redirect('/posts/')