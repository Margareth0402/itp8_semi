from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required

def hell(request):
    return HttpResponse("Hello world!")

def login_view(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Logandssign.html', {'theme': theme})

def home_view(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'Home.html', {'theme': theme})

def signup_view(request):
    theme = request.session.get('theme', 'light')
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Logandssign.html', {'theme': theme})

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
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.address = request.POST['address']
        user.gender = request.POST['gender']
        user.birthday = request.POST['birthday']
        user.save()
        return redirect('user_account')
    return HttpResponse("Invalid request", status=400)

def toggle_theme(request):
    current_theme = request.session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    request.session['theme'] = new_theme
    return redirect(request.META.get('HTTP_REFERER', 'home'))



def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book, status='in_cart')
    cart_item.quantity += quantity
    cart_item.save()
    return redirect('shopping_cart')

def buy_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.status = 'bought'
    item.save()
    return redirect('user_account')

def bookstore_inventory(request):
    # Retrieve all books from the database (replace with your actual model logic)
    books = Book.objects.all()
    return render(request, 'bookstore/inventory.html', {'books': books})