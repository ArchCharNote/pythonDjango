from django.db import models

# Create your models here.
class Family(models.Model):
    # Family - bear
    name = models.CharField(max_length=64)
    

class Kind(models.Model):
    #View animal - White bear
    pass

class AnimalCard(models.Model):
    pass

class Food(models.Model):
    pass

# class Animals(models.Model):
#     #UserName
#     name = models.CharField(max_length=40)
#
#     #age
#     age = models.PositiveIntegerField()
#     #type
#     # type =
#     #food
#     food = models.TextField()
#
#     def __str__(self):
#         return self.name