from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    context = models.TextField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    isbn = models.CharField(max_length=13)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
