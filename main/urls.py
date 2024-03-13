from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# registering model view sets
# the router function is important because it generates routes for all the class functions
router.register(r'queries',QueryModelViewSet,basename='queries')

urlpatterns = [
    path("schedules/fetch/",fetch_class_schedules),
    path("schedules/create/",create_class_schedule),
    path('',include(router.urls))
]