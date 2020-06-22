from django.db import models


# Create your models here.


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

    def __str__(self):
        return self.title
