from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Discussion model
class Discussion(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ribbit_discussion")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='discussion_likes', blank=True)
    down_vote = models.ManyToManyField(
        User, related_name='discussion_downvote', blank=True)
    category = models.CharField(max_length=100, default='coding')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_down_vote(self):
        return self.down_vote.count()

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    Discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(User, max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Categorys(models.Model):
    name = models.CharField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
