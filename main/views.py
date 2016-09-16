from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
import pdb;

@login_required()
def index(request):
    productList = Product.objects.order_by('-id')[:5]
    context = {
        'productList': productList,
    }
    return render(request, 'list.html', context)

@login_required()
def detail(request, productId):
    product = get_object_or_404(Product, pk=productId)
    return render(request, 'detail.html', {'product': product})

@login_required()
def cart(request):
    if request.method == 'POST':
        cartItem = Cart(user_id=request.user.id, product_id=request.POST['product_id'], quantity=request.POST['quantity'])
        cartItem.save()
        return redirect('cart')
    else:
        cartItems = Cart.objects.filter(user_id=request.user.id)
        return render(request, 'cart.html', {'cartItems': cartItems})

    