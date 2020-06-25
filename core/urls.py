from django.urls import path


from .views import BlogView, \
    BlogDetailView, \
          AboutView, \
    IndexView, \
    BlogCreateView, \
    BlogUpdateView, \
    BlogDeleteView, \
    ViewBlog, \
    ContactCreateView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('blog/', BlogView.as_view(), name='blog_view'),
    path('blog-detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('add-blog/', BlogCreateView.as_view(), name='add_blog'),
    path('update-blog/<slug:slug>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete-blog/<slug:slug>', BlogDeleteView.as_view(), name='delete-blog'),
    path('view-blog', ViewBlog.as_view(), name='view-blog'),
   ]
