from tkinter import CASCADE
from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(
        # "auth.User",
        # 'settings.AUTH_USER_MODEL', ## add after creating custom users
        # #on_delete=models.CASCADE,
        # )
    
    body = models.TextField()

    
    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.author
    

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    