from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from math import ceil
# Create your views here.
def index(request):
    #products=Product.objects.all()
    #n=len(products)
    #no_slide=n//4 + ceil(n/4 -(n//4))
   # dict={'products':allproducts,'rangeproducts':range(1,no_slide),'noofslides':no_slide}
    # allprodct=[[products,range(1,len(products)),no_slide],
              # [products,range(1,len(products)),no_slide]]
    allprodct=[]
    catgry=Product.objects.values('category','id')
    catgrys={item['category'] for item in catgry }
    for cat in catgrys:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        no_slide = n // 4 + ceil(n / 4 - (n // 4))
        allprodct.append([prod, range(1, no_slide), no_slide])

    dict={'allprodct':allprodct}

    return render(request,'store/index.html',dict)

def about(request):
    return render(request,'store/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        descviews = request.POST.get('descht', '')
        contact=Contact(name=name,phone=phone,email=email,descdata=descviews)

        contact.save()


    return render(request,'store/contact.html')
def seller(request):
    if request.method=="POST":
        productname=request.POST.get('prodname','')
        category = request.POST.get('category', '')
        subcategory = request.POST.get('subcategory', '')
        descv = request.POST.get('descht1', '')
        productdate=request.POST.get('proddate', '')
        price=request.POST.get('amount', '')
        image=request.POST.get('image','')
        product=Product(product_name=productname,category=category,subcategory=subcategory,desc=descv,product_date=productdate,price=price,image=image)
        product.save()

    return render(request,'store/Seller.html')
def search(request):
    #query=request.GET('query')
    #allname=Product.objects.all()
    #psara={'allname':allname}
    return render(request,'store/search.html',psara)
def prodView(request,getid):
    prod1= Product.objects.filter(id=getid)

    return render(request,'store/productview.html',{'productshow':prod1[0]})
def checkout(request):
    return render(request,'store/checkout.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname = request.POST['firstname']
        lname= request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        confirmpass = request.POST['confirmpass']
        print(username)
        if len(username)>10:
            messages.error(request,"Too long password,Fill a password less than 10 characters!")
            return redirect('/store')
        if pass1!=confirmpass:
            messages.error(request,"wrong password!,Try Again")
            return redirect('/store')
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save();
        messages.success(request, "Your profile is successfully created!")

        return redirect('/store')
    else:
        return HTTpResponse("404 Not Found")

def handlelogin(request):
    if request.method =='POST':
        namelogin=request.POST['namelogin']
        passwordlogin = request.POST['passwordlogin']

        customer=authenticate(username=namelogin,password=passwordlogin)
        if customer is not None:
            login(request,customer)
            messages.success(request,"You are successfully loged in!")
            return redirect('/store')
        else:
            messages.error(request,"Wrong Credentials,Try again!")
            return redirect( '/store')
    return HTTpResponse('404 error')

def handlelogout(request):
    logout(request)
    messages.success(request, "You are successfully loged out!")
    return redirect('/store')

    return HTTpResponse('404 error')

