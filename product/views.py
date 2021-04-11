from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductsView(ListView):
    template_name = 'product/list_products.html'
    def get_queryset(self):
        product = Product.objects.all()
        return product


class ProductsAddView(CreateView):
    model = Product
    fields = (
        'name', 'slug',
        'price',
        'image', 'thumbnail',
        'category'
    )
    success_url = reverse_lazy('products')
    # success_message = "Produto adicionado com sucesso!"
    form_valid_message = 'O Produto foi criado com successo!'

class ProductsUpdateView(UpdateView):
    model = Product
    fields = (
        'name', 'slug',
        'price',
        'image', 'thumbnail',
        'category'
    )
    success_url = reverse_lazy('products')
    form_valid_message = "Produto adicionada com sucesso!"


class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class CategoryList(ListView):
    template_name = 'product/list_categories.html'
    def get_queryset(self):
        category = Category.objects.all()
        return category


class CategoriesAddView(CreateView):
    model = Category
    fields = ('name', 'slug',)
    success_url = reverse_lazy('categories')
    success_message = "Categoria adicionada com sucesso!"


class CategoriesUpdateView(UpdateView):
    model = Category
    fields = ('name', 'slug',)
    success_url = reverse_lazy('categories')
    form_valid_message = "Categoria adicionada com sucesso!"


class CategoriesDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})