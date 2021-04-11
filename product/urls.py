from django.urls import path, include

from product import views

urlpatterns = [
    # path('latest-products/', views.LatestProductsList.as_view()),
    # Product
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/add', views.ProductsAddView.as_view(), name='add_product'),
    path('products/<int:pk>/update', views.ProductsUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete', views.ProductsDeleteView.as_view(), name='delete_product'),
    # Category
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/add', views.CategoriesAddView.as_view(), name='add_category'),
    path('categories/<int:pk>/update', views.CategoriesUpdateView.as_view(), name='update_category'),
    path('categories/<int:pk>/delete', views.CategoriesDeleteView.as_view(), name='delete_category'),
    # API
    path('', views.ProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]