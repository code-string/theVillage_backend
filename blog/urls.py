from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.view_posts, name='view_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    # path('<int:post_id>/share/', views.post_share, name='post_share')
]

