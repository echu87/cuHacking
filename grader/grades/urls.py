
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('classroom', views.classroom, name='classroom'),
<<<<<<< HEAD
    path('cclass', views.classroom_create, name='classroom_create'),
    path('jclass', views.join_class,name='join_class'),
    path('dclass',views.dclass,name = "delete class"),
=======
    path('classroom/<int:project_number>', views.classroom, name='classroom'),
>>>>>>> origin/matt
]