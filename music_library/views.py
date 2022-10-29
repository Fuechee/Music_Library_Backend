from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

# Create your views here.
@api_view(['GET','POST'])
def songs(request):
    if request.method == 'GET':
        query_set = Song.objects.all()
        serailizer = SongSerializer(query_set, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serailizer = SongSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response(serailizer.data, status=status.HTTP_201_CREATED)