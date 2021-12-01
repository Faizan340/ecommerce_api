from django.urls import path
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct
urlpatterns=[ 
    path('categories',ListCategory.as_view(),name='Category'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='SingleCategory'),
    path('books',ListBook.as_view(),name='Book'),
    path('books/<int:pk>/',DetailBook.as_view(),name='SingleBook'),
    path('products',ListProduct.as_view(),name='Product'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='SingleProduct')
]