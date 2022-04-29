from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce import HTMLField

# Create your models here.


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_image = CloudinaryField('post_image', blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__ (self):
        return self.title

    def get_absoulute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    