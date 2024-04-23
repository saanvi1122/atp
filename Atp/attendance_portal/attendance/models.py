from django.db import models

class Attendance(models.Model):
    employee_id = models.IntegerField()
    date = models.DateField()
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
