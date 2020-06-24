from django.urls import path


from .views import BlogView, \
    BlogDetailView, \
    ContactView, \
    AboutView, \
    IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('blog/', BlogView.as_view(), name='blog_view'),
    path('blog-detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),


]
