from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('create_products', views.create_products, name='create_products'),
    path('<int:pk>', views.ShopDetailView.as_view(), name="shop-detail"),
    path('<int:pk>/update', views.ShopUpdateView.as_view(), name="products-update"),
    path('<int:pk>/delete', views.ShopDeleteView.as_view(), name="products-delete"),
    path('search/', views.search.as_view(), name='search_shop')
]
