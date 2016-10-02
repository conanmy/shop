from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/$', views.index, name='index'),
    url(r'^product/(?P<productId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^cart/delete$', views.cart_delete, name='cart_delete'),
    url(r'^order/$', views.order, name='order'),
    url(r'^orders/$', views.orders, name='orders'),
]