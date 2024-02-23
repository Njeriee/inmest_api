from rest_framework import serializers

from main.models import Course
from users.serializers import CohortSerializer, UserSerializer

# refer to user models for fields

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateField()

# this is an example of a model serializer
# models serializers are slow and are therefore not recommended for many records
class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','description')
        model = Course

class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    descripttion = serializers.CharField()
    start_date_and_time = serializers.CharField()
    end_date_and_time = serializers.CharField()
    is_repeated = serializers.CharField()
    repeat_frequency = serializers.CharField()
    organizer = UserSerializer(many = False)
    meeting_type = serializers.CharField()
    fascilitator = serializers.CharField()
    venue = serializers.CharField()
    course = CourseSerializer(many = False)
    cohort = CohortSerializer(many = False)
    date_created = serializers.DateTimeField()

# class AttendanceSerializer(serializers.Serializer):




