from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


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
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]

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

    def get_absolute_url1(self):
        return reverse("core:update_blog", kwargs={
            'slug': self.slug
        })

    def get_absolute_url2(self):
        return reverse("core:delete-blog", kwargs={
            'slug': self.slug
        })


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name