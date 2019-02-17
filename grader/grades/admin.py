from django.contrib import admin
from .models import Classroom, Task, Marks

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Task)
admin.site.register(Marks)
