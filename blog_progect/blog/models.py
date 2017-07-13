# python3
# blog_project/blog/models.py
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    """
    Posts model.
    Methods:
        publish
        approve_comments
        get_absolute_url
    """
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Recording time in "published_date" published.
        """
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        """
        Approve comments.
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comments model.
    Methods:
        approve
    """
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """
        Approve comments
        """
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
