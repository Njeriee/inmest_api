from django.urls import path
from .views import *

urlpatterns = [
    path("schedules/fetch/",fetch_class_schedules),
    path("schedules/create/",create_class_schedule)
]