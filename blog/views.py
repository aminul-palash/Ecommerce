from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,Http404
from bookmanagement.models import Book,Comments
from blog.models import BlogPost
from bookmanagement.forms import CommentsForm
from django.views.generic import (
  ListView,DeleteView,DetailView
)

# Create your views here.
class BlogListView(ListView):
  model=BlogPost
  template_name='blog/allblog.html'


def BlogDetailView(request,pk):
    object = get_object_or_404(BlogPost,pk=pk)
    comment = Comments.objects.filter(blog=object)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            content = form.save(commit=False)
            content.commented_by = request.user
            content.blog = object
            content.save()
            return redirect('blog:detail',pk )
        else:
            #redirect('accounts:login')
            #raise Http404
            return redirect('accounts:login')
            
    else:
        form = CommentsForm()
    context = {
           'object':object,
           'form':form,
           'comment':comment,
        }
    
    return render(request,'blog/blog_detail.html',context)
	