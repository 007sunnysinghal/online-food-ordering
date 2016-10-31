from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
