from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.

def user_login(request):
	mess = ''
	if (request.method == 'POST'):
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			if user:
				if user.is_active:
					login(request, user)
					#Redirect 
				else:
					mess = 'Disabled Account'
			else:
				mess = 'Invalid Login'

	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form, 'mess': mess})


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})