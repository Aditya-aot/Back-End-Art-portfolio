from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Artwork
from .serializers import ArtworkSerializer

class ArtworkListView(generics.ListAPIView):
    queryset = Artwork.objects.all().order_by('-order')
    serializer_class = ArtworkSerializer
