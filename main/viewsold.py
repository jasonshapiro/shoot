from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from main.models import *

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('base.html')

def submit(request):
    return render_to_response('submit.html')

def latest(request):
    idea_title_form = request.POST['idea_title']
    idea_text_form = request.POST['idea_text']
    idea_created_form = datetime.datetime.now()
    idea_last_activity_form = datetime.datetime.now()
    idea = Idea(idea_title=idea_title_form, idea_text=idea_text_form, idea_created=idea_created_form, 
                idea_last_activity=idea_last_activity_form)
    idea.save()

    return HttpResponseRedirect('/')


def index(request):
    
    ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
    allcomments = []
    for eachidea in ideas:
        comments = Comment.objects.filter(idea=eachidea)
        allcomments = [allcomments,comments]

    return render_to_response('index.html',context_instance=RequestContext(request, {'ideaslist':ideas, 'commentlist':allcomments}))
