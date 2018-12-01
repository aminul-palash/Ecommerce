from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bookmanagement.models import BookTransactionModel
from profiles.models import Profile
from profiles.forms import ProfileForm




class ShowProfile(generic.TemplateView):
    template_name = "profiles/show_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booklog'] =  BookTransactionModel.objects.all().filter(lend_by=self.request.user)
        return context
    

        
class EditProfile(LoginRequiredMixin, UpdateView):
    model=Profile
    form_class=ProfileForm
    template_name = "profiles/edit_profile.html"

    def get_success_url(self):
        return reverse('profiles:show_self')
