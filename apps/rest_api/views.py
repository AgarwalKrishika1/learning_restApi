from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ViewSetMixin, GenericViewSet, ModelViewSet
from apps.rest_api.models import Books
# from models import Books
from apps.rest_api.serializer import BooksSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Create your views here.

# def BooksView(request):
#     if request.method == 'GET':
#         posts = Books.objects.all()
#         serializer = BooksSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BooksSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=404)

class BooksViewSet(GenericViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data, safe=False)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return JsonResponse(serializer.data, status=201)

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Books.objects.filter(email=user_object.email).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookModelViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
