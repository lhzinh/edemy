from accounts.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
