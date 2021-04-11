from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product import views
from product import api

urlpatterns = [
    path('latest-products/', api.ProductsList.as_view()),
    # path('latest-products/', api.LatestProductsList.as_view()),
    # Product
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/add', views.ProductsAddView.as_view(), name='add_product'),
    path('products/<int:pk>/update', views.ProductsUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/details', views.ProductsDetailsView.as_view(), name='detail_product'),
    path('products/<int:pk>/delete', views.ProductsDeleteView.as_view(), name='delete_product'),
    # Category
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/add', views.CategoriesAddView.as_view(), name='add_category'),
    path('categories/<int:pk>/update', views.CategoriesUpdateView.as_view(), name='update_category'),
    path('categories/<int:pk>/delete', views.CategoriesDeleteView.as_view(), name='delete_category'),
    # API
    path('', api.ProductsList.as_view()),
    path('products/search/', api.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', api.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', api.CategoryDetail.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
