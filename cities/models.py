from django.db import models
from django.db.models import Avg
from django.shortcuts import get_object_or_404

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('id',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    country = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    region = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='cities', blank=True, null=True)
    population = models.BigIntegerField(blank=False, null=True)
    average_rating = models.FloatField(default=0)

    class Meta:
        db_table = 'city'
        verbose_name = 'city'
        verbose_name_plural = 'cities'
        ordering = ('id',)


    def update_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = ratings.aggregate(models.Avg('rating'))['rating__avg']
        else:
            self.average_rating = 0
        self.save()

    def get_average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    def get_total_count(self):
        return self.ratings.count()

    def __str__(self):
        return f'Name: {self.name}, Country: {self.country}'


class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='attrs', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    categories = models.ManyToManyField(Category, related_name='attractions')

    class Meta:
        db_table = 'attraction'
        verbose_name = 'attraction'
        verbose_name_plural = 'attractions'
        ordering = ('id',)

    def __str__(self):
        return f'Name: {self.name}, City: {self.city}, Categories: {self.categories}'


class Rating(models.Model):
    city = models.ForeignKey(City, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('city', 'user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.city.update_average_rating()
