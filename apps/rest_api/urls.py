from django.urls import path, include
from apps.rest_api.views import BooksViewSet, BookModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'bookmodel', BookModelViewSet, basename='modelbooks')

urlpatterns = [
    path('', include(router.urls))
]
