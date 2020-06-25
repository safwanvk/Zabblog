from django import forms
from django.views.generic.edit import ModelFormMixin

from .models import Blog, Contact


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
            'category',
            'image',
            'slug'
        ]


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'