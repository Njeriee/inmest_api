from django.contrib import admin

from users.models import *

# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("name","date_created","date_modified")

admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)