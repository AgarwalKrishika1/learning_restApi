from rest_framework import serializers
from apps.rest_api.models import Books, Album, Runner


class BooksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=10, allow_null=False, allow_blank=False)
    # def title_validate(self, title):
    #     if (title < 10):
    #         raise serializers.ValidationError("Title of book is wrong")
    #     return title
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'price', 'email']


class AlbumSerializer(serializers.ModelSerializer):
    model1 = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Books.objects.all())

    class Meta:
        model = Album
        fields = ['model1', 'artist', 'name', 'release_date']

# class RunnerSerializer(serializers.HyperlinkedModelSerializer):
#     AlbumSerializer.serializer_related_field = BooksSerializer


class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner
        fields = ['name', 'medal']
