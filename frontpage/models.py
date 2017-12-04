from django.db import models

# Create your models here.


class Carousel(models.Model):
    # carousel_image = models.ImageField(upload_to='media/carousels/%Y', blank=False)
    carousel_header = models.CharField(max_length=200, db_index=True)
    carousel_body = models.CharField(max_length=200, db_index=True)


class Blogpost(models.Model):
    post_heading = models.CharField(max_length=200, db_index=True)
    post_body = models.TextField(db_index=True)
    post_picture = models.ImageField(upload_to='blogpost/%Y', blank=False)
    created = models.DateTimeField(auto_now_add=True)

