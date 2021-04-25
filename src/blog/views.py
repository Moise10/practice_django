from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import BlogPost
from .forms import Blog_post_form , BlogPostModelForm

# Create your views here.


def blog_post_list_view(request):
  # list all the objects exple: qs = BlogPost.objects.filter(slug__contains = "hello")
  # could be search
  qs = BlogPost.objects.all() # -> list all the objects
  template_name = "blog/list.html"
  context = {"object_list": qs}
  return render(request, template_name, context)


def blog_post_detail_view(request, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = "blog/detail.html"
  context = {"object": obj}
  return render(request, template_name, context)

@login_required
@staff_member_required
def blog_post_create_view(request):
  # create objects
  # use a form
  form = BlogPostModelForm(request.POST)
  if form.is_valid():
    form.save()
    form = BlogPostModelForm()
  template_name = "blog/form.html"
  context = {'form': form}
  return render(request, template_name, context)

@login_required
@staff_member_required
def blog_post_update_view(request, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = "blog/form.html"
  form = BlogPostModelForm(request.POST or None, instance=obj)
  context = {'form': form, 'object': obj, "title": f"Update {obj.title}"}
  return render(request, template_name, context)


def blog_post_delete_view(request, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = "blog/delete.html"
  context = {'object': obj}
  if request.method == 'POST':
    obj.delete()
    return redirect('/blog')
  return render(request, template_name, context)

