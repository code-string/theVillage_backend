from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.registration, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('login', views.login_user, name='login'),
     path('update', views.update_acount, name='update'),


    
]