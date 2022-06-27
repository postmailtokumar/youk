from django.db import models


class Employee(models.Model):

    emp_id = models.IntegerField()
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)

    class Meta:
        ordering = ('emp_id',)

    def __str__(self):
        return self.name
