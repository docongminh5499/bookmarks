from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm

urlpatterns = [
		#path('login/', views.user_login, name = 'login')
		url(r'login', auth_view.LoginView.as_view(template_name = 'account/login.html', authentication_form = LoginForm), name = 'login'),
		url(r'logout', auth_view.LogoutView.as_view(template_name = 'account/logout.html'), name = 'logout'),
		url(r'dashboard', views.dashboard, name = 'dashboard'),
		url(r'password_change', auth_view.PasswordChangeView.as_view(template_name = 'account/password_change.html', success_url = reverse_lazy('account:password_change_done')), name = 'password_change'),
		url(r'password_change_done', auth_view.PasswordChangeDoneView.as_view(template_name = 'account/password_change_done.html'), name = 'password_change_done')

]