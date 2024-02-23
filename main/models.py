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
    MEETING_TYPES = (
        ('CLASS_SESSIONS','Class Sessions'),
        ('WELLNESS_SESSIONS','Wellness seesions'),
        ('GUEST_LECTURE','Guest lecture')
    )

    REPEAT_FREQUENCY = (
        ('DAILY','Daily'),
        ('WEEKLY','Weekly'),
        ('MONTHLY','Monthly')
    )
    title = models.CharField(max_length = 100)
    description = models.TextField(default = 'N/A',blank = True,null = True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField
    is_repeated = models.BooleanField()
    repeat_frequency = models.CharField(max_length = 20, choices = REPEAT_FREQUENCY,blank = True,null = True)
    is_active = models.BooleanField()
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = 'class_organizer')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,blank = True,null = True)
    facillitator = models.ForeignKey(IMUser, on_delete=models.SET_NULL,blank = True,null = True,related_name = 'class_facillitator')
    meeting_type = models.CharField(max_length = 20, choices = MEETING_TYPES,blank = True,null = True)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)

    def __str__(self):
        return f"{self.name}"

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='class_attendance_author')

    def __str__(self):
        return f"{self.name}"

class Query(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='query_submitter')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='query_assignee')
    resolution_status = models.TextChoices("PENDING","IN_PROGRESS","DECLINED","RESOLVED")
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='query_author')

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


# create 3 cohorts and 6 IMUsers and assign 2 users each cohort
# create users since chort inherits from users
# create a variable called author and assign it to a user object
# eg author=IMUser.objects.get(id=1)
# now pass the author into the cohort object
# Cohort.objects.create(author=author)