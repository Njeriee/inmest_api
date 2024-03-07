from django.db import models
from django.contrib.auth.models import *
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# signals are used to listen and perform tasks when an event happens
from django.db.models.signals import post_save

# Create your models here.
# update the IMUser model to have the following keys is_blocked,temporal_login_field = interger field and permernent_login_field = integer field
# is_blocked = boolean field,perform migrations and update the login function in the views
class IMUser(AbstractUser):
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    # unique code is for reseting passwords or otp 
    # do not add it to the serializer
    unique_code = models.CharField(max_length=20,blank=True)

    USER_TYPES = [
        ('EIT', 'Entrepreneur in training'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='imuser_set',blank=True)
    is_blocked = models.BooleanField(default = True)
    temporal_login_field = models.IntegerField(default = 0)
    permernent_login_field = models.IntegerField(default = 0)
    
    def _str_(self):
        return f"{self.first_name} {self.last_name}"
    
# token generation function
@receiver(post_save,sender=IMUser)
def generate_user_auth_token(sender,instance=None,created=False, **kwargs):
    if created :
            token = Token.objects.create(user=instance)
            token.save()

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



