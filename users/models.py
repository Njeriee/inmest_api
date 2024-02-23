from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class IMUser(AbstractUser):
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    USER_TYPES = [
        ('EIT', 'Entrepreneur in training'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT')
    date_created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='imuser_set')
    
    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class Cohort(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohort_author')

    def __str__(self):
        return f"{self.name}"

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohort_member_author')

    def __str__(self):
        return f"{self.name}"


