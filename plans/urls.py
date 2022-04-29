from django.urls import path

from . import views


app_name = 'plans'

urlpatterns = [
    path('', views.plan_list, name='plan_list'),
    # path('<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('<int:plan_id>/<str:plan_title>/<int:plan_price>/', views.plan_detail, name='plan_detail'),

    
]