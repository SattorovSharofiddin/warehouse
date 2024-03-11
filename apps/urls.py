from django.urls import path

from apps.views import ProductMaterialsView

urlpatterns = [
    path('products/', ProductMaterialsView.as_view(), name='product-list'),
]
