from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AuthForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .forms import AuthForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.user.is_authenticated == True:
            return redirect('../profile/')
    if request.method == 'POST':
        user_form = AuthForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            print(request.user.is_authenticated)
            return redirect('../login/')
    else:
        user_form = AuthForm()
        return render(request, 'auth/reg.html', {'user_form': user_form})


@login_required(login_url='../login/')
def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('../profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    print(request.user.is_authenticated)
    return render(request, 'auth/profile.html', context)