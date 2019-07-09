from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    @staticmethod
    def get_author(obj):
        return obj.author.name