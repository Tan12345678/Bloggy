from django.db import models
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=600)
    content=models.TextField()
    pub_date=models.DateTimeField('DATE PUBLISHED')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])  # Adjust the URL name accordingly

    def __str__(self):
        return self.title
# Create your models here.
