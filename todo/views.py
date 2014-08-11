from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from todo.models import Task
from todo.forms import TodoForm

import logging

log = logging.getLogger(__name__)

@login_required(login_url='/admin/')
def list(request):
	tasks = Task.objects.filter(created_by=request.user).all()
	return render_to_response("todo/list.html", RequestContext(request, {"tasks": tasks}))

@login_required(login_url='/admin/')
def create(request):
	name = request.POST.get('name')

	task = Task(name=name, created_by=request.user)
	task.save()
	
	return redirect("/")
