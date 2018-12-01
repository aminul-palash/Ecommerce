from django.urls import path
from django.conf.urls import url
from bookmanagement import views
from bookmanagement.views import BookListView,BookDetailView 

app_name = 'bookmanagement'
urlpatterns = [
    url(r'^$',BookListView.as_view(),name='booklist'),
    url(r'^(?P<pk>\d+)/$', views.BookDetailView, name='detail' ),
]
 