from rest_framework import serializers
from apps.rest_api.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'price', 'email']
