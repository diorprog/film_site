from django.urls import path

from .views import home, categories, amime_details, anime_watching, blog, blog_details, login, register, contacts, shop, \
    cart

urlpatterns = [
    path('', home, name='home'),
    path('categories', categories, name='categories'),
    path('anime-details', amime_details, name='categories'),
    path('anime-watching', anime_watching, name='categories'),
    path('blog', blog, name='blog'),
    path('blog-details', blog_details, name='categories'),
    path('login', login, name='categories'),
    path('register', register, name='categories'),
    path('contacts', contacts, name='contacts'),
    path('shop', shop, name='shop'),
    path('cart', cart, name='cart')
]
