from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='No description provided')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



from django.db import models

class SignUpData(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
