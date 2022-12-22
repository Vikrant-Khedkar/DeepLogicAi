from django.db import models

# Create your models here.

class data(models.Model):
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.pdf
        

