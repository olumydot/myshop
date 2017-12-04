from django.shortcuts import render
from shop.models import Category, Product
from .models import Blogpost, Carousel


def landing_view(request):

    blog = Blogpost.objects.all()
    carousel = Carousel.objects.all()
    carousel1 = Carousel.objects.all().get(pk=1)
    carousel2 = Carousel.objects.all().get(pk=2)
    carousel3 = Carousel.objects.all().get(pk=3)
    products = Product.objects.filter(available=True)

    return render(request, 'frontpage/landing/index.html', {'blog': blog,
                                                      'carousel1': carousel1,
                                                      'carousel2': carousel2,
                                                      'carousel3': carousel3,
                                                      'products': products,
                                                       })
