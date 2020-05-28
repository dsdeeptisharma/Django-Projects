from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request,"website/welcome.html",#{"message":"This data was sent by view to Template"}
     #{"num_meetings":Meeting.objects.count()}
    {"meetings":Meeting.objects.all()})
  #  return HttpResponse("Welcome to the Meeting Planner Website!")



def date(request):
    return HttpResponse("This page was served at:" + str(datetime.now()))

def about(request):
    return HttpResponse("I am new to Django and looking forward to get better in this.")

