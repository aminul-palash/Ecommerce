from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
    path('me/', views.ShowProfile.as_view(), name='show_self'),
    #path('me/edit/', views.EditProfile.as_view(), name='edit_self'),
    url(r'^me/(?P<pk>\d+)/$', views.EditProfile.as_view(), name='update' ),
    
]
