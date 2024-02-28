import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from main.serialzers import *

# QUERY SETS
# Create your views here.
# filter is used when you want to retreive many items and returns an array while get is for a specific item
# use filter when you want to implement a search function

# Course.objects.get(name="Comms") - returns the object comms
# Course.objects.filter(name_of_db_entry__contains="e") 
# Course.objects.create()- creates an instance of data 
# cohort_member = CohortMember.objects.create(cohort = cohort,member = user_three,author = user_three, is_active = True)

@api_view(["GET"])
def fetch_class_schedules(request):
    # 1. Retrieve class schedules from the database
    queryset = ClassSchedule.objects.all()

    # 2. Return queryset results as response
    # 2b. serialize the queryset results to json and send as response

    serializer = ClassScheduleSerializer(queryset,many = True)

    # 3.respond to the request
    return Response({"data":serializer.data},status.HTTP_200_OK)

@api_view(["POST"])
def create_class_schedule(request):
    title = request.data.get("title")
    description = request.data.get("description")
    start_date_and_time = datetime.datetime.now
    end_date_and_time = datetime.datetime.now
    cohort_id = request.data.get("cohort_id")
    venue = request.data.get("venue")
    fascillitator_id = request.data.get("fascillitator_id")
    is_repeated = request.data.get("is_repeated")
    repeat_frequency = request.data.get("repeat_frequency")
    course_id = request.data.get("course_id")
    meeting_type = request.data.get("meeting_type")

    # performing validations
    if not title:
        return Response({"message":"my friend send title"},status.HTTP_400_BAD_REQUEST)
    if not start_date_and_time:
        return Response({"message":"my friend send start_date_and_time"},status.HTTP_400_BAD_REQUEST)
    if not end_date_and_time:
        return Response({"message":"my friend send end_date_and_time"},status.HTTP_400_BAD_REQUEST)

    cohort = None
    fascillitator = None
    course = None

    # validating the existance of records
    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({"message":"this cohort does not exist"},status.HTTP_400_BAD_REQUEST)
    
    try:
        fascillitator = IMUser.objects.get(id=fascillitator_id)
    except IMUser.DoesNotExist:
        return Response({"message":"this fascillitator does not exist"},status.HTTP_400_BAD_REQUEST)
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message":"this course does not exist"},status.HTTP_400_BAD_REQUEST)
    
    class_schedule = ClassSchedule.objects.create(
        title = title,
        description = description,
        venue = venue,
        is_repeated = is_repeated,
        repeat_frequency = repeat_frequency,
        fascillitator = fascillitator,
        cohort = cohort,
        course = course,
        organizer = fascillitator,
        meeting_type = meeting_type

    )
    class_schedule.save()

    serializer = ClassScheduleSerializer(many = False)
    return Response({"message":"schedule successfully created","data":serializer.data},status.HTTP_200_OK)


