
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('main', views.homepage, name='homepage'),
    path('cclass', views.classroom_create, name='classroom_create'),
=======
    path('', views.homepage, name='homepage'),
    path('classroom', views.classroom, name='classroom')
>>>>>>> origin/matt
]