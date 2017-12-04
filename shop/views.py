from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Subscription
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # image = products.images.all().filter(pk=1)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list2.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                       })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail2.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                    })


def sub_create(request):
    if request.method == 'POST':
        form = SubCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            sub = Subscription(email=email)
            sub.save()

    return render(request, 'shop/base.html', {'form': form})


