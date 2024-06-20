from django.urls import path
from Backend import views
urlpatterns = [
    path('indexpage/',views.indexpage, name="indexpage"),
    path('catpage/', views.catpage, name="catpage"),
    path('savdata/', views.savdata, name="savdata"),
    path('buyerdisplay/', views.buyerdisplay, name="buyerdisplay"),
    path('sellerdisplay/', views.sellerdisplay, name="sellerdisplay"),
    path('orderdisplay/',views.orderdisplay, name="orderdisplay"),
    path('paymentdisplay/', views.paymentdisplay, name="paymentdisplay"),
    path('feedback/', views.feedback, name="feedback"),
    path('admin_login/',views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/',views.admin_logout, name="admin_logout"),
    path('product_display/',views.product_display,name="product_display"),
    path('edit_pro/<int:dataid>',views.edit_pro,name="edit_pro"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deletepro/<int:dataid>/',views.deletepro,name="deletepro"),
    path('deletesell/<int:dataid>/',views.deletesell,name="deletesell"),
    ]