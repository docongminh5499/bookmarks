from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, Register
# Create your views here.


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
	if (request.method == 'POST'):
		user_form = Register(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit = False)
			new_user.set_password(user_form.cleaned_data['password1'])
			new_user.save()
			return render(request, 'account/register_done.html', {'user': new_user})
	else:
		user_form = Register()
	return render(request, 'account/register.html', {'form': user_form})