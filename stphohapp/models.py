from django.db import models

class Patient(models.Model):
    first = models.CharField(max_length=55, default="")
    last = models.CharField(max_length=55, default="")
    state = models.CharField(max_length=255, default="")
    age = models.CharField(max_length=15, default="")
    sex = models.CharField(max_length=15, default="")
    phone = models.CharField(max_length=15, default="")
    result = models.ForeignKey('Result', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Patient Info: " + self.first + " " + self.last 

class Result(models.Model):
    hiv_aid_test = models.CharField(max_length=100, )
    hepatitis_B_test = models.CharField(max_length=100, )
    