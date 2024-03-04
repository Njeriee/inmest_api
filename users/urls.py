

from django.urls import path
from users.views import *


urlpatterns = [
    # path("say_hello/",say_hello),
    path("signup/",signup)
    # path("user_query/<str:name>",user_query),
    # path("login/",UserViewSet.as_view())
]