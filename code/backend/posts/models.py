from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    
    ## doing this will show Post Title in Django admin site
    def __str__(self):
        return self.text[:50]
