from django.contrib import messages
from django.shortcuts import render,redirect
from Backend.models import ProductDB
from Frontend.models import ContactDB,SellDB
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def indexpage(req):
    return render(req,"index.html")

def catpage(req):
    return render(req,"Products.html")

def savdata(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        des = req.POST.get('description')
        img = req.FILES.get('image')
        obj = ProductDB(Product_Name=cn, Description=des, Cat_Image=img)
        obj.save()
        messages.success(req,"Product Added Successfully....!")
        return redirect(catpage)

def buyerdisplay(req):
    # data = ShopDB.objects.all()
    return render(req, "Buyer_View.html")




def orderdisplay(req):
    # data = ShopDB.objects.all()
    return render(req, "order_item.html")

def paymentdisplay(req):
    # data = ShopDB.objects.all()
    return render(req, "payment_details.html")

def admin_login(req):
    return render(req,"AdminLogin.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect('indexpage')  # Assuming 'indexpage' is the name of the URL pattern
            else:
                return render(request, 'adminlogin.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'adminlogin.html', {'error': 'User does not exist'})
    else:
        return render(request, 'adminlogin.html')

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def product_display(req):
    data = ProductDB.objects.all()
    return render(req,"product_dis.html",{'data':data})

def edit_pro(req,dataid):
    data=ProductDB.objects.get(id=dataid)
    return render(req,"edit_pro.html",{'data':data})

def updateproduct(req,dataid):
     if req.method == "POST":
            name = req.POST.get('cname')
            desp = req.POST.get('description')
            try: 
                img =req.FILES['image']
                fs = FileSystemStorage()
                file = fs.save(img.name,img)
            except MultiValueDictKeyError:
                file = ProductDB.objects.get(id=dataid).Cat_Image
            ProductDB.objects.filter(id=dataid).update(Product_Name=name,Description=desp,Cat_Image=file)
            messages.success(req,"Product Updated Successfully....!")
            return redirect(product_display)

def deletepro(req,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Product Deleted Successfully....!")
    return redirect(product_display)

def sellerdisplay(req):
    data = SellDB.objects.all()
    return render(req, "Seller_View.html",{'data':data})

def deletesell(req,dataid):
    data = SellDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Deleted Successfully....!")
    return redirect(sellerdisplay)

def feedback(req):
    data = ContactDB.objects.all()
    return render(req, "feedback.html",{'data':data})

