from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField() 
    due_date = models.DateField()  #YYYY-MM-DD
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title 
