from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    # def get_context_data(self,**kwargs):
    #     context  = super().get_context_data(**kwargs)
    #     context['injectme'] = "Basic Injection!"
    #     return context

class PostsListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    template_name='index.html'
    model=models.Posts



class PostsDetailView(DetailView):
    context_object_name = 'posts_details'
    model = models.Posts
    template_name = 'CBVs/posts_detail.html'


class PostsCreateView(CreateView):
    

    fields = '__all__'
    model = models.Posts


class PostsUpdateView(UpdateView):
    fields = '__all__'
    model = models.Posts

class PostsDeleteView(DeleteView):
    model = models.Posts
    success_url = reverse_lazy("CBVs:list")
