from django.urls import path, re_path, include
from django.conf.urls import url
from . import views

urlpatterns = [
		path(r'login', views.user_login, name = 'login')
		#url(r'login', login)
]