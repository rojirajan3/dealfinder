from django.urls import path
from Frontend import views

urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('home2page/', views.home2page, name= "home2page"),
        path('sellpage/', views.sellpage,name= "sellpage"),
        path('savedata/', views.savedata, name="savedata"),
        path('singlepage/<int:proid>/', views.singlepage, name='singlepage'),

        path('cartpage/', views.cartpage, name= "cartpage"),
        path('footerpage/', views.footerpage, name= "footerpage"),
        path('conpage/', views.conpage, name= "conpage"),
        path('savecon/', views.savecon, name="savecon"),
        path('protpage/', views.protpage, name="protpage"),
        path('regpage/', views.regpage, name="regpage"),
        path('savereg/', views.savereg, name="savereg"),
        path('login_page/', views.login_page, name="login_page"),
        path('user_login/', views.user_login, name="user_login"),
        path('user_logout/', views.user_logout, name="user_logout"),
        path('filtered_page/<product_name>/',views.filtered_page,name='filtered_page'),
        path('about/', views.about, name="about"),
        path('userhome/', views.userhome, name="userhome"),
        path('profile/', views.profile, name="profile"),
        path('updateprofile/<int:dataid>/', views.updateprofile, name="updateprofile"),
        path('edit_page/<user_id>/', views.edit_page, name="edit_page"),
        path('deletesell/<int:dataid>/', views.deletesell, name='deletesell'),
        path('search/', views.search, name='search'),
        path('aboutpage2/', views.aboutpage2, name="aboutpage2"),
        path('verify_otp/', views.verify_otp, name='verify_otp'),
        
] 