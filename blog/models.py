from django.db import models
from django.conf import settings

from django.urls import reverse
from django.utils.text import Truncator
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class BlogPost(models.Model):
    title  = models.CharField(max_length=32)
    content = models.TextField()
    writter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete='CASECADE')
    mark = models.BooleanField(default=False)
    image = models.ImageField(upload_to='%Y/%m/%d',null=True,blank=True,default = 'blog.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk":self.pk})

