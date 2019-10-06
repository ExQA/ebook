from django.db import models

# Create your models here. Нужно описывать все функции

class Book(models.Model):
    #title price autor full_tex file
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(max_length=255)


    def __str__(self):
        return '{} {} $'.format(self.title, self.price, self.description)


