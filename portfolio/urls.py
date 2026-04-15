from django.urls import path
from .views import ArtworkListView

urlpatterns = [
    path('artworks/', ArtworkListView.as_view(), name='artworks'),
]