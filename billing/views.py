from django.views import generic
from django.shortcuts import get_object_or_404, redirect,render
from django.utils import timezone
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bookmanagement.models import BookTransactionModel,Book
from billing.forms import BillingForm
 

def payment_method_view(request,pk):
  object = get_object_or_404(Book,pk=pk)
  if request.method == 'POST':
    form = BillingForm(request.POST)
    if not request.user.is_authenticated:
      return redirect('accounts:login')
    if form.is_valid():
      content = form.save(commit=False)
      content.lend_by = request.user
      content.book = object
      content.lend_from =  timezone.now()
      content.save()
      return redirect("profiles:show_self")    
  else:
    form = BillingForm()
  return render(request,  'billing/payment_method.html', { 'object' : object ,  'form': form})
 
 