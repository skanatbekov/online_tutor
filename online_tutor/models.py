from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
