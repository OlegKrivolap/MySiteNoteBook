from django.db import models


# Create your models here.



class Note(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField(null=True)
    media = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.title