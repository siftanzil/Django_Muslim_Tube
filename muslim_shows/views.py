from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View, TemplateView


# Create your views here.


class BlogList(TemplateView):
    template_name = "App_Video/index.html"
