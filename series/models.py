from django.db import models

# Create your models here.
class Serie( models.Model ):
    title = models.CharField(max_length=50)
    description = models.TextField()

    #Se tradue en objeto a string
    def __str__(self):
        return self.title

class Episode( models.Model ):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Episode {self.number} - {self.name}'