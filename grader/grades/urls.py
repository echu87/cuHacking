
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.homepage, name='homepage'),
    path('classroom', views.classroom, name='classroom')
=======
    path('main', views.homepage, name='homepage'),
    path('cclass', views.classroom_create, name='classroom_create'),
>>>>>>> origin/youssef
]