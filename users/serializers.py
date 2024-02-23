from rest_framework import serializers

# refer to user models for fields

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()


class CohortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    author = UserSerializer(many = False)

# the business logic here is you send a list of cohort members when the frontend requests
# you can not send all the cohorts that is a lot of data
# instead you send only data for a particular cohort at a time
    
class CohortMemberSerializer(serializers.Serializer):
    member = UserSerializer(many = False)
    
    
