from django.urls import path
from .views import HomePageView, NewBkmkPageView, DetailBkmkPageView, SearchPageView, ResultsPageView


urlpatterns = [
    path("search/results/", ResultsPageView.as_view(), name="results"),
    path("search", SearchPageView.as_view(), name="search"),
    path("post/<int:pk>/", DetailBkmkPageView.as_view(), name="detail"),
    path("new", NewBkmkPageView.as_view(), name="new"),
    path("", HomePageView.as_view(), name="home"),
]
