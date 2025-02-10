from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from trendtrove.models import Product, Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                prod_id = int(request.POST.get('product_id'))
                prod_check = Product.objects.get(id=prod_id)

                if Cart.objects.filter(user=request.user, product=prod_check).exists():
                    return JsonResponse({'status': "Product Already in Cart"})
                
                prod_qty = int(request.POST.get('product_qty'))

                if prod_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product=prod_check, product_qty=prod_qty)
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    return JsonResponse({'status': f"Only {prod_check.quantity} Quantity Available"})

            except Product.DoesNotExist:
                return JsonResponse({'status': "No Such Product Found"})
        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect('/')

@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context= {'cart':cart}
    return render(request, 'trendtrove/cart.html', context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(user=request.user, product_id=prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"}) 
    return redirect('/')

def removefromcart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(user=request.user, product_id=prod_id)
            cartitem.delete()
        return JsonResponse({'status':"Deleted Successfully"}) 
    return redirect('/')
