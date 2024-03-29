from django.http import Http404
from django.views.generic  import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

class ProductFeaturedListView(ListView):
  template_name = "products/list.html"

  def get_queryset(self, *args, **kwargs):
    request = self.request
    return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
  queryset = Product.objects.all().featured()
  template_name = "products/fetured-detail.html"

  # def get_queryset(self, *args, **kwargs):
  #   request = self.request
  #   return Product.objects.featured()


class ProductListView(ListView):
  #queryset = Product.objects.all()
  template_name = "products/list.html"
  
  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductListView,self).get_context_data(*args, **kwargs)
  #   return context 

  def get_queryset(self, *args, **kwargs):
    request = self.request
    return Product.objects.all()

def product_list_view(request):
  queryset = Product.objects.all()
  context = {
       'object_list': queryset,
  }
  return render(request, "products/list.html", context)

class ProductDetailSlugView(DetailView):
  queryset = Product.objects.all()
  template_name = "products/detail.html"
  
  def get_object(self, *args, **kwargs):
    request = self.request
    slug = self.kwargs.get('slug')
    try:
      instance = Product.objects.get(slug = slug, active = True)
    except Product.DoesNotExist:
      raise Http404("Product does not exist")
    except Product.MultipleObjectsReturned:
      qs = Product.objects.filter(slug = slug, active = True)
      instance = qs.first()
    except:
      raise Http404('Something fishy')
    print(instance)
    return instance

class ProductDetailView(DetailView):
  queryset = Product.objects.all()
  template_name = "products/detail.html"
  
  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductListView,self).get_context_data(*args, **kwargs)
  #   return context 

  def get_object(self, *args, **kwargs):
    request = self.request
    pk = self.kwargs.get('pk')
    instance = Product.objects.get_by_id(pk)
    if instance is None:
      raise Http404('Product Does not Exist')


def product_detail_view(request, pk = None):
  #instance = Product.objects.get(pk=pk) #id
  #instance = get_object_or_404(Product,pk = pk)
  # try:
  #   instance = Product.objects.get(id = pk)
  # except Product.DoesNotExist:
  #   print('no product found here')
  #   raise Http404('Product Does not Exist')
  # except:
  #   print('Huh?')

  instance = Product.objects.get_by_id(pk)
  if instance is None:
    raise Http404('Product Does not Exist')

  # print(instance)

  # qs = Product.objects.filter(pk = pk)
  # if qs.exists() and qs.count() == 1:
  #   instance = qs.first()
  # else:
  #   print('no product found here')
  #   raise Http404('Product Does not Exist')

  context = {
       'object': instance,
  }
  return render(request, "products/detail.html", context)