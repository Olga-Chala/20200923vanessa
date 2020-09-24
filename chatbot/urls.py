from django.urls import path
from . import views

urlpatterns = [
    path('', views.talk, name='talk'),
#     path('post/questions/', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#     path('post/start/', views.start_vanessa, name='start_vanessa'),
#     path('post/keywords/', views.post_keys, name='post_keys'),
]