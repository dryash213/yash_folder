# myapp/models.py
from django.db import models

class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    Type = models.TextField(default='Unknown')  # Set a default value for existing and future rows
    system_prompt = models.TextField()
    prompt = models.TextField()
    model = models.TextField()

    def __str__(self):
        return f"{self.Type} - {self.system_prompt[:50]}... ({self.model})"
