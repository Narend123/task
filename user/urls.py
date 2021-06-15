from django.urls import path
from user import views

urlpatterns = [
				path('', views.home,name='home'),
				path('users', views.users,name='users'),
				path('login', views.login,name='login'),
				path('logout', views.logout,name='logout'),
				path('sign_up', views.sign_up,name='sign_up'),
				]