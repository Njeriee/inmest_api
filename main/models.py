from django.db import models

from users.models import Cohort, IMUser

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length = 100)
    description = models.TextField(default = 'N/A',blank = True,null = True)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)

    def __str__(self):
        return f"{self.name}"

class ClassSchedule(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(default = 'N/A',blank = True,null = True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField
    is_repeated = models.BooleanField()
    repeat_frequency = models.IntegerField()
    is_active = models.BooleanField()
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.name}"

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Query(models.Model):
    title = models.CharField(max_length = 100)
    description = models.Textfield()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    resolution_status = models.TextChoices("PENDING","IN_PROGRESS","DECLINED","RESOLVED")
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"