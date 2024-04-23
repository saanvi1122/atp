from django.shortcuts import render
from .models import Attendance 

def attendance_list(request):
    attendances = attendance_list.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})
