from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from Frontend.models import SellDB,RegisterDB,ContactDB
from Backend.models import ProductDB
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
import re
from django.template.loader import render_to_string


# Create your views here.
def homepage(req):
    cat = ProductDB.objects.all()
    return render(req, "Home.html", {'cat': cat})

def userhome(request):
    cat = ProductDB.objects.all()
    user_id = request.user.id
    return render(request, "user.html", {'cat': cat, 'user_id': user_id})

def home2page(req):
    cat = ProductDB.objects.all()
    pro = SellDB.objects.all()
    return render(req, "Home2.html", {'cat': cat, 'pro': pro})

def footerpage(req):
    return render(req, "Footer.html")

def singlepage(request, proid):
    product = get_object_or_404(SellDB, id=proid)
    return render(request, 'singleproduct.html', {'product': product, 'proid': proid})

def conpage(request):
    return render(request,"Contact.html")

def savecon(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('mobile')
        msg = request.POST.get('msg')
        obj = ContactDB(Name=n, Email=e, Mobile=m, Feedback=msg)
        obj.save()
        return redirect(conpage)



def regpage(request):
    return render(request,"Register.html")

def generate_otp():
    return random.randint(100000, 999999)

def savereg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        # Password validation regex
        password_pattern = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        )

        if not password_pattern.match(pwd):
            messages.error(request, "Password must be at least 8 characters long, include uppercase and lowercase letters, symbols, and numeric digits.")
            return render(request, "Register.html")

        if RegisterDB.objects.filter(Username=un).exists():
            return HttpResponse("Username already taken")
        if RegisterDB.objects.filter(Email=em).exists():
            return HttpResponse("Email already registered")

        request.session['name'] = na
        request.session['email'] = em
        request.session['username'] = un
        request.session['password'] = pwd

        otp = generate_otp()
        request.session['registration_otp'] = otp

        send_mail(
            'Welcome to Deal Finder',
            f"""
            Welcome to Deal Finder!

            You can sell or buy your items here.

            Here is your 6-digit OTP number: {otp}

            Enjoy the site!

            All the best,
            
            Deal Finder Admin Panel

            Thank you for choosing us.
            """,
            settings.EMAIL_HOST_USER,
            [em],
            fail_silently=False,
        )

        return redirect('verify_otp')
    return render(request, "Register.html")

def verify_otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        if otp == str(request.session.get('registration_otp')):
            # Retrieve user info from session
            na = request.session.get('name')
            em = request.session.get('email')
            un = request.session.get('username')
            pwd = request.session.get('password')

            # Save user to the database
            obj = RegisterDB(Name=na, Email=em, Username=un, Password=pwd)
            obj.save()

            # Clear session data
            request.session.flush()

            return redirect('login_page')
        else:
            return HttpResponse("Invalid OTP")
    return render(request, "verify_otp.html")


def login_page(request):
    return render(request,"Login.html")

 
# def user_login(request):
#     if request.method == "POST":
#         un = request.POST.get('username')
#         pwd = request.POST.get('password')
#         try:
#             user = RegisterDB.objects.get(Username=un, Password=pwd)
#             request.session['Username'] = user.Username
#             request.session['UserId'] = user.UserId
            
#             return redirect('userhome')
#         except RegisterDB.DoesNotExist:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login_page')
#     return redirect('login_page')

# def user_login(request):
#     if request.method == "POST":
#         un = request.POST.get('username')
#         pwd = request.POST.get('password')
#         try:
#             user = RegisterDB.objects.get(Username=un, Password=pwd)
#             request.session['Username'] = user.Username
#             request.session['UserId'] = user.UserId
            
#             # Add a success message
            
#             return redirect('userhome')
#         except RegisterDB.DoesNotExist:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login_page')
#     return redirect('login_page')

def user_logout(request):
    if 'Username' in request.session:
        del request.session['Username']
    if 'Password' in request.session:
        del request.session['Password']
    return redirect(homepage)

def sellpage(req):
    category = ProductDB.objects.all()
    return render(req, "Sell_Product.html", {'category': category})

def protpage(request):
    pro_list = SellDB.objects.all()
    paginator = Paginator(pro_list, 20)  # Show 20 products per page

    page_number = request.GET.get('page')
    pro = paginator.get_page(page_number)
    return render(request, "Product.html", {'pro': pro})

# def savedata(request):
#     if request.method == "POST":
#         p = request.POST.get('cname')
#         pn = request.POST.get('pname')
#         mob = request.POST.get('number')
#         n = request.POST.get('name')
#         email = request.POST.get('email')
#         des = request.POST.get('description')
#         pri = request.POST.get('price')
#         img = request.FILES.get('image')
#         obj = SellDB(product=p, product_name=pn, mobile=mob, name=n, email=email, description=des, price=pri, product_image=img)
#         obj.save()
#         return redirect('homepage')

def savedata(request):
    if request.method == "POST":
        user_id = request.session.get('UserId')
        if user_id is None:
            messages.error(request, "User is not logged in.")
            return redirect('login_page')

        p = request.POST.get('cname')
        pn = request.POST.get('pname')
        mob = request.POST.get('number')
        n = request.POST.get('name')
        email = request.POST.get('email')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        img = request.FILES.get('image')

        try:
            user = RegisterDB.objects.get(UserId=user_id)
            obj = SellDB(
                product=p,
                product_name=pn,
                mobile=mob,
                name=n,
                email=email,
                description=des,
                price=pri,
                product_image=img,
                UserId=user
            )
            obj.save()

            # Render the email template with the product details
            email_content = render_to_string('product_sold_email.html', {'product': obj})

            # Send an email notification to the seller
            send_mail(
                'Your Product Has Been Listed',
                '',
                settings.EMAIL_HOST_USER,
                [user.Email],
                fail_silently=False,
                html_message=email_content
            )

            messages.success(request, "Product saved successfully! A confirmation email has been sent.")
            return redirect('userhome')
        except RegisterDB.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('login_page')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('sellpage')

    return render(request, 'Sell_Product.html')



def filtered_page(request, product_name):
    pro = SellDB.objects.filter(product=product_name)  # Ensure 'product' matches the model's field name
    return render(request, "product_filtered.html", {'pro': pro})

def about(request):
    return render(request,"about.html")


def profile(request):
    data = RegisterDB.objects.filter(UserId=request.session['UserId'])
    return render(request,"Profile.html",{'data':data})

def edit_page(request, user_id):
    # Use user_id to fetch the data
    data = get_object_or_404(RegisterDB, UserId=user_id)
    return render(request, "edit_profile.html", {'data': data})

def updateprofile(request, dataid):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        un = request.POST.get('username')
        RegisterDB.objects.filter(UserId=dataid).update(Name=n, Email=e, Username=un)
        messages.success(request, "Profile Edited Successfully..!")
 
        return redirect(userhome)

# @login_required
def cartpage(request):
    user_id = request.session.get('UserId')
    if user_id:
        data = SellDB.objects.filter(UserId=user_id)
        return render(request, "shoping_cart.html", {'data': data})
    # else:
    #     messages.error(request, "User ID not found in session.")
    #     return redirect('login_page')



def deletesell(req,dataid):
    data = SellDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Deleted Successfully....!")
    return redirect('cartpage')

def search(request):
    query = request.POST.get('product', '')
    if query:
        results = SellDB.objects.filter(product_name__icontains=query)
    else:
        results = SellDB.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})



def aboutpage2(request):
    return render(request,"about2.html")



def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user = RegisterDB.objects.get(Username=un, Password=pwd)
            request.session['Username'] = user.Username
            request.session['UserId'] = user.UserId

            # Render the email template with the user's username
            email_content = render_to_string('welcome_email.html', {'username': user.Username})

            # Send welcome email
            send_mail(
                'Welcome to Deal Finder',
                '',
                settings.EMAIL_HOST_USER,
                [user.Email],
                fail_silently=False,
                html_message=email_content
            )

           
            return redirect('userhome')
        except RegisterDB.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect('login_page')
    return redirect('login_page')