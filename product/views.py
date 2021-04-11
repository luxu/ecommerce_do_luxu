from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Product, Category


class ProductsView(ListView):
    template_name = 'product/list_products.html'
    def get_queryset(self):
        product = Product.objects.all()
        return product


class ProductsAddView(CreateView):
    model = Product
    fields = (
        'name', 'price',
        'image', 'thumbnail',
        'category'
    )
    success_url = reverse_lazy('products')
    form_valid_message = 'O Produto foi criado com successo!'

class ProductsUpdateView(UpdateView):
    model = Product
    fields = (
        'name', 'price',
        'image', 'thumbnail',
        'category'
    )
    success_url = reverse_lazy('products')
    form_valid_message = "Produto adicionado com sucesso!"



class ProductsDetailsView(DetailView):
    queryset = Product.objects.all()

    def get_queryset(self):
        """Filter product_id"""
        product = self.queryset.filter(id=self.kwargs.get('pk'))
        return product

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
    fields = ('name',)
    success_url = reverse_lazy('categories')
    success_message = "Categoria adicionada com sucesso!"


class CategoriesUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('categories')
    form_valid_message = "Categoria adicionada com sucesso!"


class CategoriesDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
