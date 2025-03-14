from django.db import models

class File(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    file = models.FileField(upload_to='uploads/', default='example.txt')

    def __str__(self):
        return self.name 
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

