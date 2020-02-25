from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=280)
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note Title: {self.title} Body: {self.body}"
