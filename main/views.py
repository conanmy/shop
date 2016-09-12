from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

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