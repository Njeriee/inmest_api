

from django.urls import path
from users.views import *


urlpatterns = [
    # path("say_hello/",say_hello),
    path("signup/",signup),
    # path("user_query/<str:name>",user_query),
    # path("login/",UserViewSet.as_view()),
    path("forgot_password/",ForgotPasswordAPIView.as_view()),
    path('reset_password/',ResetPassword.as_view()),
    path('me/',CurrentUserProfile.as_view())
]