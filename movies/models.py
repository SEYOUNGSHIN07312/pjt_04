from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRE = (('공포','공포'), ('코미디','코미디'), ('로맨스', '로맨스'),)
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30, choices=GENRE)
    score = models.FloatField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True)