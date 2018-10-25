from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    STATUS = (
        ('PENDING', 'pending'),
        ('COMPLETED', 'completed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title =  models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS)
    updated_on = models.DateTimeField(auto_now=True)