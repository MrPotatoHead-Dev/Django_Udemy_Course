from django.db import models

# Create your models here.
class Topic (models.Model):

    top_name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.top_name
    

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AcessRecords(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()


    def __str__(self) -> str:
        return self.date