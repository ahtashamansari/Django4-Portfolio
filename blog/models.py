from django.db import models

# Create your models here.

class visitor(models.Model):
    first_name = models.CharField(max_length = 40)
    second_name = models.CharField(max_length = 40)

    def __str__(self):
        return self.first_name

class contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length = 150)
    messages = models.TextField()

    def __str__(self):
        return self.name  

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100] 

    def __str__(self):
        return self.title

class Project_detail(models.Model):
    project_name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.project_name                       

