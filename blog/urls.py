from django.urls import path
from django.conf.urls import url
from blog import views
from blog.views import BlogListView,BlogDetailView 

app_name = 'blog'
urlpatterns = [
    url(r'^$',BlogListView.as_view(),name='bloglist'),
    url(r'^(?P<pk>\d+)/$', views.BlogDetailView, name='detail' ),
]
  