from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def complete(self):
    	self.completed = True
    	super(Task, self).save()
