from django.shortcuts import render, redirect
from .models import Carusel, CategoryL0, CategoryL1, Contact, Product
from .forms import ContactForm, NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
import random
# Create your views here.


class IndexListView(ListView):
    template_name = 'main/index.html'

    def get(self, request):
        carusel_active = Carusel.objects.all()[0]
        carusel = Carusel.objects.all()[1:]
        categoryl0 = CategoryL0.objects.all()
        categoryl1 = CategoryL1.objects.all()
        prods = Product.objects.all()

        return render(request, self.template_name, context={
            'carusel_active': carusel_active,
            'carusel': carusel,
            'categoryl0':categoryl0,
            'categoryl1':categoryl1,
            'prods':prods,
        })


class Index_detailListView(ListView):
    template_name = 'main/index_detail.html'

    def get(self, request, id):
        carusel_active = Carusel.objects.all()[0]
        carusel = Carusel.objects.all()[1:]
        categoryl0 = CategoryL0.objects.all()
        categoryl1 = CategoryL1.objects.all()
        categoryl1_filter = CategoryL1.objects.filter(pk=id)
        prods = Product.objects.all()
        return render(request, self.template_name , context={
            'carusel_active': carusel_active,
            'carusel': carusel,
            'categoryl0':categoryl0,
            'categoryl1':categoryl1,
            'categoryl1_filter':categoryl1_filter,
            'prods':prods,
        })
    

class Product_detailsDetailView(DetailView):
    template_name = 'main/product-details.html'

    def get(self, request, id):
        categoryl0 = CategoryL0.objects.all()
        categoryl1 = CategoryL1.objects.all()
        prods = Product.objects.all()
        obj = Product.objects.get(pk=id)
        return render(request, self.template_name, context={
            'obj': obj,
            'categoryl0':categoryl0,
            'categoryl1':categoryl1,
            'prods':prods
        })





def product_details_admin(request, id):
    # x = User.objects.get(pk=id)
    # if not x.username:
    #     link = 'Error'
    #     return redirect('index')
    # if not user.is_authenticated:???????????????????????????????????????????????????????????
    #       return redirect('product_detail')?????????????????????????????????????????????????

    categoryl0 = CategoryL0.objects.all()
    categoryl1 = CategoryL1.objects.all()
    prods = Product.objects.all()
    obj = Product.objects.get(pk=id)
    if request.method == 'POST':
        new_head = request.POST.get('head')
        new_price = request.POST.get('price')
        try:
            new_price = int(new_price)
            x = Product.objects.get(pk=id)
            x.price = new_price
            x.head = new_head
            x.save()
            return redirect('product_detail', id)
        except:
                return redirect('product_detail')
    return render(request, 'main/product-details-admin.html', context={
        'obj': obj,
        'categoryl0':categoryl0,
        'categoryl1':categoryl1,
        'prods':prods
    })



def contact_us(request):
    if request.method == 'POST':    
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('contact_us')
    else:
        form = ContactForm()
        

    return render(request, 'main/contact-us.html', context={
        'form':form
    })





def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})




def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")