from django.urls import path
from django.conf.urls import url

from billing import views as billing_views


app_name = 'billing'
urlpatterns = [
   url(r'^(?P<pk>\d+)/billing/$', billing_views.payment_method_view, name='bookbill'),
]
