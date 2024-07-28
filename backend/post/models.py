from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=500, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=250, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text





