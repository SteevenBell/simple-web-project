from django.db import models


class Student(models.Model):
    name = models.CharField(name="name", max_length=240)
    email = models.EmailField()
    document = models.CharField(name="document", max_length=20)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField("registration date", auto_now_add=True)

    def __str__(self):
        return self.name
