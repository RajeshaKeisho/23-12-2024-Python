from typing import Any
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
import django_filters
from django.views.generic import ListView
from rest_framework import generics, filters

# Create your views here.
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter
    ]

    filterset_class = ProductFilter
    search_fields = ['brand__name', 'category__name', 'name', 'description']
    ordering_fields = ['name', 'price', 'stock']
    ordering = ['name']

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = ProductFilter(self.request.GET, queryset=queryset)
        queryset = self.filter.qs

        # Apply ordering
        ordering = self.request.GET.get('ordering', 'name')
        queryset = queryset.order_by(ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context
