from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,Http404
from .models import Book,Comments
from bookmanagement.forms import CommentsForm
from django.views.generic import (
  ListView,DeleteView,DetailView
)

# Create your views here.
class BookListView(ListView):
  model=Book
  template_name='bookpages/allbooks.html'
"""
class BookDetailView(DetailView):
  queryset = Book.objects.all()
  template_name= 'bookpages/book_detail.html'

"""
def BookDetailView(request,pk):
    object = get_object_or_404(Book,pk=pk)
    comment = Comments.objects.filter(book=object)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            content = form.save(commit=False)
            content.commented_by = request.user
            content.book = object
            content.save()
            return redirect('bookmanagement:detail',pk )
        else:
            #redirect('accounts:login')
            #raise Http404
            return redirect('accounts:login')
            
    else:
        form = CommentsForm()
    context = {
           'object':object,
           'comment':comment,
           'form':form,
        }
    
    return render(request,'bookpages/book_detail.html',context)
	