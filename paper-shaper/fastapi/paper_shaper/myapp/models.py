# myapp/models.py
from django.db import models

class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    Type = models.TextField()  # Set a default value for existing and future rows
    Class = models.TextField(default='random')  # Set a default value for existing and future rows
    system_prompt = models.TextField()
    prompt = models.TextField()
    model = models.TextField()

    def __str__(self):
        return f"{self.Type} - {self.system_prompt[:50]}... ({self.model})"




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
