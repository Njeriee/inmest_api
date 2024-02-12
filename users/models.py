from django.db import models

# Create your models here.
class IMUser (models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    is_active = models.BooleanField()
    user_type = models.TextChoices("EIT", "TEACHING_FELLOW","ADMIN_STAFF","ADMIN")
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)

    def __str__(self):
        return f"{self.name}"

class Cohort(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohort_author')

    def __str__(self):
        return f"{self.name}"

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    date_modified = models.DateTimeField(auto_now=True,blank = True,null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohort_member_author')

    def __str__(self):
        return f"{self.name}"