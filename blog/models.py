from django.db import models

class Blogs(models.Model):
    title=models.CharField(max_length=100)
    datetime=models.DateTimeField()
    description=models.TextField()

    def __str__(self):
        return self.title

