from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
		#path('login/', views.user_login, name = 'login')
		url(r'login', auth_view.LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
		url(r'logout', auth_view.LogoutView.as_view(template_name = 'account/logout.html'), name = 'logout'),
		url(r'dashboard', views.dashboard, name = 'dashboard'),
		
]