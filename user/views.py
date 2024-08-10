from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import UserLoginForm, RegisterForm


# Create your views here.

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Authentication'}
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login failed. Please check your username and password.')
        return super().form_invalid(form)

# def login_user(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main:main'))
#     else:
#         form = UserLoginForm()
#     return render(request, 'user/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'Account created for {user.username}')
            login(request, user)
            return redirect('main:main')
    else:
        form = RegisterForm()
    return render(request, 'user/registration.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, f'You are logged out of your account {request.user.username}')
    return HttpResponseRedirect(reverse('user:login'))
