from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .forms import BlogForm
from .models import Blog


class IndexView(ListView):
    model = Blog
    paginated_by = 10
    context_object_name = 'blogs'
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogView(ListView):
    model = Blog
    paginate_by = 10
    context_object_name = 'blogs'
    template_name = "core/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "core/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ContactView(TemplateView):
    template_name = "core/contact.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class BlogCreateView(CreateView):
    form_class = BlogForm
    template_name = 'core/add_blog.html'

    def form_valid(self, form):
        form.save()
        return redirect('/add-blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = [
        'title',
        'body',
        'category',
        'image',
        'slug'
    ]
    template_name = 'core/update_blog.html'
    success_url = '/'

