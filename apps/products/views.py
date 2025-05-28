from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from apps.categories.models import Category
from apps.products.models import Product


def homepage(request):
    categories = Category.objects.all()

    return render(request, "index.html", locals())


def list_products(request, pk):
    category = Category.objects.get(id=pk)
    products = category.products_cats.all()[::-1]

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "detail-prod.html", locals())


def search_logics(request):
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(title__icontains=query)
        
        paginator = Paginator(products, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "search.html", locals())
    
    return redirect("homepage")
