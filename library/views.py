from django.shortcuts import render
from django.views.generic.list import ListView
from bookmanagement.models import Book

# Create your views here.
class home(ListView):
  model=Book
  template_name = 'homepage/home.html'