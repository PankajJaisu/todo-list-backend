from django.db import models

# Create your models here. 
class Task(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField('Tag',null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
