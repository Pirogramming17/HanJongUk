from pyexpat import model
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    director = models.CharField(max_length=50, verbose_name="감독")
    main = models.CharField(max_length=50, verbose_name="주연")
    years = models.IntegerField(verbose_name="개봉 년도")
    genre = models.CharField(max_length=50, verbose_name="장르")
    starRating = models.FloatField(verbose_name="별점")
    runningTime = models.IntegerField(verbose_name="러닝타임")
    reviews = models.TextField(verbose_name="리뷰 내용")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(auto_now=True)