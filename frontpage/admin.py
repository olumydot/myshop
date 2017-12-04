from django.contrib import admin
from .models import Carousel, Blogpost


class CarouselAdmin (admin.ModelAdmin):
    list_display = ['carousel_header', 'carousel_body']


admin.site.register(Carousel, CarouselAdmin)


class BlogpostAdmin (admin.ModelAdmin):
    list_display = ['post_heading', 'post_body']


admin.site.register(Blogpost, BlogpostAdmin)





