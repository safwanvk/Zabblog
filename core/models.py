
from django.db import models

# Create your models here.
from django.urls import reverse


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    website = models.URLField()
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    website = models.URLField()
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    ILLUSTRATION = 'I'
    BRANDING = 'B'
    APPLICATION = 'A'
    DESIGN = 'D'
    MARKETING = 'M'
    CATEGORY_CHOICES = [
        (ILLUSTRATION, 'Illustration'),
        (BRANDING, 'Branding'),
        (APPLICATION, 'Application'),
        (DESIGN, 'Design'),
        (MARKETING, 'Marketing')
    ]
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("core:blog_detail", kwargs={
            'slug': self.slug
        })


