from typing import List
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class HomeView(TemplateView):
    template_name = "base_components/base.html"
