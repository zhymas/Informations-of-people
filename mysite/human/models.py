from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('person_detail', args=[str(self.id)])
