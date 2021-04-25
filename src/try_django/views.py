from django.http import HttpResponse
from django.shortcuts import render
from .forms import Contact_form


def home_page(request):
  title = "Hello there home page..."
  return render(request, 'home.html', {'title': title})

def contact_page(request):
  form = Contact_form(request.POST or None)
  if form.is_valid():
    form.cleaned_data
    form = Contact_form()
  context = {'title': 'Contact', 'form': form}
  return render(request, 'form.html', context)
  

def about_page(request):
  my_title = "Hello there about page ..."
  return render(request, 'about.html', {'my_title': my_title})
