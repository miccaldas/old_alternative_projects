from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Bookmarks
from .form import SearchForm
import subprocess


class HomePageView(ListView):
    model = Bookmarks
    bookmarks = Bookmarks.objects.all()
    template_name = "homepage.html"
    context_object_name = "object_list"


class NewBkmkPageView(CreateView):
    model = Bookmarks
    template_name = "new.html"
    fields = "__all__"


class DetailBkmkPageView(DetailView):
    model = Bookmarks
    template_name = "detail.html"


class SearchPageView(ListView):
    model = Bookmarks
    template_name = "search.html"

    def get_query(self, request):
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect("/results/")
        else:
            form = SearchForm()

        return render(request, "search.html", {"form": form})


class ResultsPageView(ListView):
    model = Bookmarks
    template_name = "results.html"
