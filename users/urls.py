

from django.urls import path
from users.views import *


urlpatterns = [
    # path("say_hello/",say_hello),
    path("user_profile/",user_profile),
    path("user_query/<str:name>",user_query),
    path("queries/",QueryView.as_view())
]