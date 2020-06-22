from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class BlogView(TemplateView):
    template_name = "blog.html"


class BlogDetailView(TemplateView):
    template_name = "blog-single.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"

