from django.shortcuts import render, redirect
from .models import Product, Category, Sale


def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_sales = Sale.objects.count()

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_sales': total_sales,
    }

    return render(request, 'dashboard.html', context)


def product_list(request):
    search = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()
    categories = Category.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        'products': products,
        'categories': categories,
        'search': search,
        'selected_category': category_id,
    }

    return render(request, 'products.html', context)


def product_edit(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')

        product.save()

        return redirect('product_list')

    return render(request, 'product_edit.html', {
        'product': product,
    })

def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete.html', {
        'product': product,
    })

def inventory(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'inventory.html', context)

def update_stock(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.stock = request.POST.get('stock')
        product.save()

    return redirect('inventory')

def sales(request):
    sales = Sale.objects.all().order_by('-sold_at')

    context = {
        'sales': sales,
    }

    return render(request, 'sales.html', context)

def record_sale(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(id=product_id)

        total_amount = product.price * quantity

        Sale.objects.create(
            product=product,
            quantity=quantity,
            total_amount=total_amount
        )

        product.stock -= quantity
        product.save()

        return redirect('sales')

    return render(request, 'record_sale.html', {
        'products': products,
    })

def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'categories.html', context)