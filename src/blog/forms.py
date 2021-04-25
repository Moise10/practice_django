from django import forms
from .models import BlogPost
from django.forms import ModelForm

class Blog_post_form(forms.Form):
  title = forms.CharField()
  slug = forms.SlugField()
  content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(ModelForm):
  class Meta:
    model = BlogPost
    fields = ['title', 'slug', 'content']
  
  def clean_title(self, *args, **kwargs):
    instance = self.instance
    title = self.cleaned_data.get('title')
    qs = BlogPost.objects.filter(title__contains=title)
    if instance is not None:
      qs = qs.exclude(pk=instance.pk)
    if qs.exists():
      raise forms.ValidationError('This title has already been used')
    return title
