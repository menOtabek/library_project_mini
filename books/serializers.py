from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'context', 'author', 'isbn', 'price', 'created_at', 'updated_at',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': 'Only available alphabetical characters for title'
            })

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                'status': False,
                'message': 'Book with this title and author is already exists'
            })

        return data

    def validate_price(self, price):
        if price < 0:
            raise ValidationError({
                'status': False,
                'message': 'Price can not be a negative number'
            })
        return price