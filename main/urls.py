from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^product/$', views.index, name='index'),
    url(r'^product/(?P<productId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/', views.cart, name='cart'),
]