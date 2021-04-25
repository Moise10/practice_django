from django.db import models
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
  user = models.ForeignKey(User,default=1, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  content = models.TextField(blank=True, null=True)

  def get_absolute_url(self):
    return f"/blog/{self.slug}"

  def get_edit_url(self):
    return f"/blog/{self.slug}/edit"

  def get_delete_url(self):
    return f"/blog/{self.slug}/delete"

