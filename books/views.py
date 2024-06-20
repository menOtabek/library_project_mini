from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'{len(books)} books returned',
            'books': serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        serialized_data = BookSerializer(book).data
        data = {
            'status': 'This is a book that you choose',
            'book': serialized_data
        }
        return Response(data, status=status.HTTP_200_OK)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            'status': True,
            'message': f'Book {book_saved} updated successfully'}, status=status.HTTP_200_OK)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'message': 'Object deleted'
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'message': 'Object not found'
            }, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(APIView):
    def post(self, request):
        book = request.data
        book_serializer = BookSerializer(data=book)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book, status=status.HTTP_201_CREATED)
        return Response({'message': 'Your data is invalid'})


class BookRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# view wrote with function
@api_view(['GET'])
def book_api_view(request, *args, **kvargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
