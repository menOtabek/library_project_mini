from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (BookListApiView, BookDetailApiView, BookUpdateApiView,
                    BookDeleteApiView, BookRetrieveUpdateDestroyApiView, BookListCreateApiView,
                    BookCreateApiView, BookViewSet, book_api_view)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('', BookListApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('books/<int:pk>/all/', BookRetrieveUpdateDestroyApiView.as_view()),
    path('books/book/', BookListCreateApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/', book_api_view)
]

urlpatterns += router.urls
