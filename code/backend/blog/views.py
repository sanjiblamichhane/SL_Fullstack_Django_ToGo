from pdb import post_mortem
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView

from .models import BlogPost

# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = BlogPost 
    template_name = 'post_detail.html'
    
class BlogCreateView(CreateView):
    model = BlogPost 
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']