from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import BigForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views import User



# Create your views here.
#Glavnaya stranisa
def home_page(request):
    #Dostaem dannie BD
    categories = Category.objects.all()
    products = Product.objects.all()

    #Otpravlaem dannie na Front
    context = {'products':products, 'categories':categories}


    return render(request, 'home.html', context)

#Vivod informasie o konkretnom producte
def product_page(request, pk):
    #Dostaem dannie iz BD
    product = Product.objects.get(id=pk)
    context = {'product':product}

    return render(request, 'product.html', context)
    #Peredaem dannie na front
    context = {'category':category, 'products': products}
    return render(request, 'сategory.html', context)



def category_page(request, pk):
    category = Category.objects.get(id=pk)
    context = {'category':category}
    return render(request, 'category.html', context)

#Poisk tovara
def search_product(request):
    if request.method == "POST":
        get_product = request.POST.get('search_product')
        search_products = Product.objects.filter(product_name__iregex=get_product)
        if search_products:
            context = {'products':search_products}
            return render(request, 'result_html', context)
        else:
            return redirect('/')

#Registrasiya
class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context ={'form': RegForm}
        return render(request, self.template_name, context)
    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
            return redirect('/')











