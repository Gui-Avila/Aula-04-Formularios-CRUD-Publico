from django.db import models

class Musics (models.Model):
  title = models.CharField(max_length = 50)
  artist = models.CharField(max_length = 70)
  genre = models.CharField(max_length = 20)
  launching = models.DateField()
  def __str__(self):
        return self.title

class Instruments (models.Model):
  OPTIONS =[
    ("B", 'Beginner'),
    ("M", 'Medium'),
    ("A", 'Advanced'),
  ]
  name = models.CharField(max_length = 50)
  origin = models.CharField(max_length = 70)
  quantity = models.IntegerField()
  expertise = models.CharField(max_length = 1, choices = OPTIONS)
  def __str__(self):
        return self.name
  
class Bands (models.Model):
  name = models.CharField(max_length = 50)
  origin = models.CharField(max_length = 70)
  genre = models.CharField(max_length = 20)
  def __str__(self):
        return self.name


