from django.urls import path
from . import views
from trendtrove.controller import authview, cart, wishlist, checkout

urlpatterns = [
    path('', views.home, name='home'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productview'),

    path('product-list', views.productlist),

    path('searchproducts', views.searchproducts, name='searchproducts'),

    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logoutpage'),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name='cart'),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('remove-from-cart', cart.removefromcart, name='removefromcart'),
    
    path('wishlist/', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name='addtowishlist'),
    path('remove-from-wishlist', wishlist.removefromwishlist, name='removefromwishlist'),

    path('checkout', checkout.index, name='checkout'),
    path(' place-order/', checkout.placeorder, name='placeorder'),
   
    ]
