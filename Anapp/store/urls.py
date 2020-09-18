
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="storehome"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contactus"),
    path("Seller/", views.seller, name="sellerid"),                  #Seller/ is the html file name not the function name
    path("search/", views.search, name="searchbar"),
    path("productview/<int:getid>", views.prodView, name="productview1"),
    path("checkout/", views.checkout, name="checkout"),
    path("signup/", views.signup, name="signup"),
path("handlelogin/", views.handlelogin, name="handlelogin"),
path("handlelogout/", views.handlelogout, name="handlelogout")


]