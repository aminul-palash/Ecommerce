from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.urls import reverse
from django.utils.text import Truncator
from profiles.models import Profile
from blog.models import BlogPost
import datetime
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
User = get_user_model()


transaction_status_choice = {
  ("Pending","Pending"),
  ("Refund","Refund"),
  ("Not Refund","Not Refund"),
}


LANGUAGE_CHOICES = (
("BANGLA", "Bangla"),
("ENGLISH", "English"),
("ARABIC","Arabic"),
("URDU", "Urdu"),
)
CATEGORY_CHOICES = (
("Spirituality", "Spirituality"),
("Tafseer", "Tafseer"),
("Hadith","Hadith"),
("Aqeedah", "Aqeedah"),
)
PUBLICATION_CHOICES = (
  ("None","None"),
   ("A","A"),
   ("B","B"),
   ("C","C"),
)

# Create your models here.
class BookOwner(models.Model):
    name            = models.CharField(max_length=32)
    phone_number    = models.CharField(max_length=17, blank=True) # validators should be a list
    address         = models.CharField(max_length=32)
    email           = models.EmailField()

    def __str__(self):
        return str(self.name)


class  	Author(models.Model):
    name     = models.CharField(max_length=32)
    about    = models.TextField()

    def __str__(self):
        return str(self.name)



class Book(models.Model):
    title            = models.CharField(max_length=32)
    language         = models.CharField(max_length=32,choices=LANGUAGE_CHOICES,default="BANGLA")
    category         = models.CharField(max_length=32,choices=CATEGORY_CHOICES,default="Spirituality")
    publication      = models.CharField(max_length=32,choices = PUBLICATION_CHOICES,default="None")
    details          = models.TextField()
    mark             = models.BooleanField(default=False)
    Author           = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='author_model')
    owner            = models.ForeignKey('BookOwner',on_delete=models.CASCADE,related_name='book_owner')
    image            = models.ImageField(upload_to='%Y/%m/%d',null=True,blank=True,default = 'book1.jpeg')
    #comments = models.ForeignKey('Comments',on_delete='CASECADE',null=True,blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("bookmanagement:detail", kwargs={"pk":self.pk})

    

class Comments(models.Model):
    comment = models.TextField()
    book = models.ForeignKey(Book,on_delete='CASECADE',null=True)
    blog = models.ForeignKey(BlogPost,on_delete='CASECADE',null=True)
    reply = models.ForeignKey('Comments',null=True,related_name='replies',on_delete='CASECADE',blank=True)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete='CASECADE')
    #user_pic = models.ForeignKey('Profile',on_delete='CASECADE',null=True,blank=True,default = 'ello.jpg')
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        truncated_message = Truncator(self.comment)
        return truncated_message.chars(30)
    
   




class BookTransactionModel(models.Model):
    book                 = models.ForeignKey(Book, on_delete=models.CASCADE,blank=True, null=True)
    lend_by            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, blank=True)
    status                = models.CharField(max_length=32,choices=transaction_status_choice,default="Pending")
    lend_from         = models.DateField(auto_now_add=True)
    address              = models.CharField(max_length=100,blank=False)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{0,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number  = models.CharField(max_length=17, blank=False) # validators should be a list
    message  = models.TextField(blank=False)

    def __str__(self):
        return str(self.book)






class QuotationFromBook(models.Model):
    """
    Class descirbes specific quotation from the book
    saved by specific user
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,blank=False, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank=False, null=False)
    quotation = models.CharField(max_length=600, null=False, blank=False)
    creation_date = models.DateField(blank=False, null=False)




   
        