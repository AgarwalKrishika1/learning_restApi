from django.shortcuts import render

from apps.rest_api.models import Books
# from models import Books
from apps.rest_api.serializer import BooksSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def BooksView(request):
    if request.method == 'GET':
        posts = Books.objects.all()
        serializer = BooksSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BooksSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
