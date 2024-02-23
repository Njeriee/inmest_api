from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


from users.models import IMUser

# Create your views here.

users = [
    {
        "id":1,
        "name":"batman",
        "realname":"Bruise Wayne",
        "city":"Gotham"
    },
        {
        "id":2,
        "name":"superman",
        "realname":"Clark Kent",
        "city":"New York"
    },
        {
        "id":3,
        "name":"the flash",
        "realname":"Barry Allen",
        "city":"Kisumu"
    }
]

def user_profile(request):
    return JsonResponse(users[2])


def user_query(request,name):
    for user in users:
        if user['name'] == name:
            return JsonResponse(user)
        
def user_filter(request,id):
   query = {
        "id": id,
        "title":"hey there"
    }
   return JsonResponse(query)

# class based views can be used to create views with more than one function
# you can handle all the view requests using class based views

class QueryView(View):
    def get(self,request):
        return JsonResponse({"result":users})
    
    def post(self,request):
        return JsonResponse({"status":"ok"})


def signup(request):
    username = request.POST["username"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone_number = request.POST("phone_number")
    password = request.POST["password"]

    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number

    )

    new_user.set_password(password)
    new_user.save()