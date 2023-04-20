from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns=[
    path('', views.IndexListView.as_view(), name='index'),
    path('brand/<int:id>/', views.Index_detailListView.as_view(), name='index_detail'),
    path('prod/<int:id>/', views.Product_detailsDetailView.as_view(), name='product_detail'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('prod/<int:id>/chenge', views.product_details_admin, name='product_detail_admin'),

]