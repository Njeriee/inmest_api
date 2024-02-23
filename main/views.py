from django.shortcuts import render


# QUERY SETS
# Create your views here.
# filter is used when you want to retreive many items and returns an array while get is for a specific item
# use filter when you want to implement a search function

# Course.objects.get(name="Comms") - returns the object comms
# Course.objects.filter(name_of_db_entry__contains="e") 
# Course.objects.create()- creates an instance of data 
# cohort_member = CohortMember.objects.create(cohort = cohort,member = user_three,author = user_three, is_active = True)

