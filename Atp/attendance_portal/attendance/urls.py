from django.contrib import admin
from django.urls import path
from .views import attendance_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("attendance/", attendance_list, name='attendance_list'),
]