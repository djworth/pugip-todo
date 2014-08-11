from django.forms import Form, CharField, ModelForm
from todo.models import Task

class TodoForm(ModelForm):
	class Meta:
		model = Task
		fields = ['name']