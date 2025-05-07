"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from body.views import add_to_cart, bookstore_inventory, buy_item, hell, login_view, home_view, signup_view, book_listing
from body.views import book_detail, update_user_info, toggle_theme, shopping_cart, user_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Library/', hell),
    
    path('log/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('listing/', book_listing, name='book_listing'),
    path('detail/', book_detail, name='book_detail'),
    path('cart/',shopping_cart, name='shopping_cart'),
    path('account/', user_account, name='user_account'),
    
    path('update_user_info/', update_user_info, name='update_user_info'),  path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('toggle-theme/', toggle_theme, name='toggle_theme'),  # URL for toggling theme
    
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('inventory/', bookstore_inventory, name='bookstore_inventory'),

    
]

