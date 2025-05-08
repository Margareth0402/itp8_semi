from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()  # Ensure this field exists
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()


    def __str__(self):
        return self.title

class CartItem(models.Model):
    STATUS_CHOICES = [
        ('in_cart', 'In Cart'),
        ('pending', 'Pending Payment'),
        ('bought', 'Bought'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_cart')
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.status}"
