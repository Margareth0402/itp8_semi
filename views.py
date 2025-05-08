
from django.shortcuts import get_object_or_404, render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import logout  # <-- Add this import
from django.contrib.auth.decorators import login_required


def custom_logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want
def hell(request):
    return HttpResponse("Hello world!")

    
def login_view(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Logandssign.html', {'theme': theme})

def signup_view(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Logandssign.html', {'theme': theme})

def home_view(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'Home.html', {'theme': theme})

def book_listing(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'BookListingPage.html', {'theme': theme})

def book_detail(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'BookDetailPage.html', {'theme': theme})

def shopping_cart(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'ShoppingCartPage.html', {'theme': theme})

def user_account(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'UserAccountPage.html', {'theme': theme})

def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('name', user.first_name)
        user.email = request.POST.get('email', user.email)
        # You may need a profile model if storing address, gender, birthday
        user.save()
        return redirect('user_account')
    return HttpResponse("Invalid request", status=400)

def toggle_theme(request):
    current_theme = request.session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    request.session['theme'] = new_theme
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book, status='in_cart')
    cart_item.quantity += quantity
    cart_item.save()
    return redirect('shopping_cart')

@login_required
def buy_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.status = 'bought'
    item.save()
    return redirect('user_account')

def bookstore_inventory(request):
    books = Book.objects.all()
    return render(request, 'bookstore/inventory.html', {'books': books})

def custom_logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want the user to go after logout


def logout_view(request):
    logout(request)
    return redirect('login')  # 'login' should match the name in your urls.py


