from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from trendtrove.models import Wishlist, Product



@login_required(login_url='loginpage')
def index(request):
    wishlist =  Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request, 'trendtrove/wishlist.html', context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST['product_id'])
            prod_check = Product.objects.get(id=prod_id)
            if(prod_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already Exist in the Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product Added to Wishlist"})
            else:
                return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login To Continue"})

    return redirect('/')

def removefromwishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST['product_id'])
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product Removed From Wishlist"})
            else:
                return JsonResponse({'status':"Product Not Found in Wishlist"})
        else:
            return JsonResponse({'status':"Login To Continue"})
    return redirect('/')