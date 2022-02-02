from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AccountPageView(TemplateView):
    template_name = 'account.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'
