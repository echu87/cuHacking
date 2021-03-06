
from django.urls import path

from . import views

urlpatterns = [
    path('cstask/<int:class_id>',views.create_task, name = 'create_task'),
    path('', views.homepage, name='homepage'),
    path('classroom', views.classroom, name='classroom'),
    path('classroom/<int:project_number>', views.classroom_detail, name='classroom_detail'),
    path('delete/<int:class_id>',views.delete_class,name = 'class_delete'),
    path('unenroll/<int:class_id>',views.enroll_class,name = 'enroll_class'),
   # path('unenroll/<int:class_id>/<int:task_id>',views.mark,name = 'mark'),
   

]