from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
    model= Entry
    template_name='Blog/index.html'
    context_object_name="entries"
    ordering=['-entry_date']
    paginate_by= 3

class DetailsView(LoginRequiredMixin, DetailView):
    model= Entry
    template_name='Blog/entryDetail.html'
class CreateEntryView(LoginRequiredMixin, CreateView):
    model= Entry
    template_name='BLog/createEntry.html'
    fields=['entry_title','entry_list']
    def form_valid(self,form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)