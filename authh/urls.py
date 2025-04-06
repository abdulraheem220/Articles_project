from django.urls import path
from . import views



urlpatterns=[
    path('', views.user_login, name='user_login'),
    path('user_register', views.user_register, name='user_register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('changepass/',views.changepass,name='changepass'),
]