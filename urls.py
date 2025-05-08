from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views
from body.views import custom_logout_view, logout_view
from body.views import (
    add_to_cart, bookstore_inventory, buy_item, hell,
    login_view, home_view, signup_view, book_listing,
    book_detail, update_user_info, toggle_theme, 
    shopping_cart, user_account, 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Library/', hell),

    path('log/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('listing/', book_listing, name='book_listing'),
    path('detail/', book_detail, name='book_detail'),
    path('cart/', shopping_cart, name='shopping_cart'),
    path('account/', user_account, name='user_account'),

    path('update_user_info/', update_user_info, name='update_user_info'),
    path('toggle-theme/', toggle_theme, name='toggle_theme'),

    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('inventory/', bookstore_inventory, name='bookstore_inventory'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', custom_logout_view, name='logout'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

]




