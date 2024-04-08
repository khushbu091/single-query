from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.IntegerField()
    City = models.CharField(max_length=100)

    class Meta:
        db_table = 'Student'
        verbose_name_plural ="Student"
    def __str__(self):
        return(self.Name)
        
