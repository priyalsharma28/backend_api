from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100)  # e.g., IT, Non-IT, etc.
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
