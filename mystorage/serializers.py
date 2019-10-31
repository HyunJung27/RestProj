from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author= serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author')


class ImageSerializer(serializers.ModelSerializer):
    author= serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)
    #이미지를 업로드하고 이미지의 결과값을(잘 올라갔는지 확인작업을) url로 하겠다.

    class Meta:
        model = Album
        fields = ('pk', 'author', 'image', 'desc')


class FileSerializer(serializers.ModelSerializer):
    author= serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk', 'author', 'myfile', 'desc')
