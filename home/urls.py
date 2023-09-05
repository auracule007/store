from django.urls import path
from . import views

urlpatterns = [
    # path('browser', views, name="template"),
    path('', views.index, name="index"),
    path('product/', views.product, name="product"),
    path('details/<slug:slug>/', views.details, name="details"),
    path('category/<slug:slug>/', views.category, name="category"),
    path('allcat/', views.allcat, name="allcat"),
    path('search/', views.search, name="search"),

    path('contact/', views.contact, name="contact"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),

    path('profile/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),
    path('password/', views.password, name="password"),

    path('shopcart/', views.shopcart, name="shopcart"),
    path('displaycart/', views.displaycart, name="displaycart"),
    path('change/', views.change, name="change"),
    path('deleteitem/', views.deleteitem, name="deleteitem"),

    path('checkout/', views.checkout, name="checkout"),
    path('pay/', views.pay, name="pay"),
    path('callback/', views.callback, name="callback"),

]


# Models -- models.py, admin.py, forms.py

# V ---- views.py , urls.py 

# T --- Tempaltes, browser