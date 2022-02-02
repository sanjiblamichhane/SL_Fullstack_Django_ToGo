from django.views.generic import ListView
from .models import BlogPost

# Create your views here.
class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'all_posts_list' 