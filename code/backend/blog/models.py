from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(
        #"auth.User",
        # 'settings.AUTH_USER_MODEL',
        #   verbose_name=_(""),
        #on_delete=models.CASCADE
        #)
    body = models.TextField()

    
    def __str__(self):
        return self.title
    
    