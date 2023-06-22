from django.urls import path
from apps.rest_api import models
from apps.rest_api.views import BooksView

urlpatterns = [

    path('posts/', BooksView)
]