
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('classroom', views.classroom, name='classroom'),
    path('classroom/<int:project_number>', views.classroom, name='classroom'),
    path('coloring/<int:project_number>', views.coloring, name='classroom'),

]