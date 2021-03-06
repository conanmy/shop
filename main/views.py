from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, Record
from django.contrib.auth.models import User
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
        product = Product.objects.get(id=request.POST['product_id'])
        user = User.objects.get(id=request.user.id)
        cartItem = Cart(user=user, product=product, quantity=request.POST['quantity'])
        cartItem.save()
        return redirect('cart')
    else:
        cartItems = Cart.objects.filter(user_id=request.user.id)
        return render(request, 'cart.html', {'cartItems': cartItems})

@login_required()
def cart_delete(request):
    cartItem = Cart.objects.get(id=request.POST['cart_item_id'])
    cartItem.delete()
    return HttpResponse('Success')

@login_required()
def order(request):
    orderInfo = request.POST
    user = User.objects.get(id=request.user.id)
    order = Order(
        user=user,
        buyerName=orderInfo['buyerName'],
        buyerEmail=orderInfo['buyerEmail'],
        buyerPhoneNumber=orderInfo['buyerPhoneNumber'],
        buyerAddress=orderInfo['buyerAddress']
    )
    order.save()
    cart_item_id_prefix = 'cart_item-'
    recordList = []
    for attr, value in request.POST.items():
        if attr.startswith(cart_item_id_prefix):
            product = Product.objects.get(id=int(attr[len(cart_item_id_prefix):]))
            record = Record(
                order=order,
                product=product,
                productName=product.productName,
                retailPrice=product.retailPrice,
                quantity=value
            )
            record.save()
            recordList.append(record)
    user.product_set.clear()
    return render(request, 'order_success.html', {'recordList': recordList })

@login_required()
def orders(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'order_list.html', {'orderList': user.order_set.all() })