from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Index(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home/index.html', {'products': products})

    def post(self, request):
        pass

    def put(self, request):
        pass


class About(View):

    def get(self, request):
        temp_object = OurTeam.objects
        all_team = temp_object.all()
        count = temp_object.count()
        return render(request, 'home/about.html', {'teams': all_team, 'count': count})

    def post(self, request):
        pass

    def put(self, request):
        pass


class Menu(View):

    def get(self, request):
        all_categories = Category.objects.all().orderby('id')
        product = Product.objects.all()
        return render(request, 'home/services.html', {'category': all_categories, 'products': product, 'meranaam': 'Deepak Verma'})

    def post(self, request):
        pass

    def put(self, request):
        pass


class Contact(View):

    def get(self, request):
        return render(request, 'home/contact.html', {})

    def post(self, request):
        pass

    def put(self, request):
        pass


class Login(View):

    def get(self, request):
        if 'user' in request.session:
            return redirect('/')
        return render(request, 'home/login.html', {'error': ''})

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = Users.objects.filter(username=username, password=password)
        if user.count() == 1:
            actual_data = user.get()
            # request.session['user'] = actual_data
            request.session['user'] = {'id': actual_data.id, 'username': actual_data.username, 'full_name': actual_data.full_name, 'email': actual_data.email, 'mobile': actual_data.mobile, 'is_logged_in': True}
            return redirect('/')
        else:
            return render(request, 'home/login.html', {'error': 'User login failed.'})


class Register(View):

    def get(self, request):
        return render(request, 'home/register.html', {})

    def post(self, request):
        full_name = request.POST.get('full_name', None)
        username = request.POST.get('username', None)
        mobile = request.POST.get('mobile', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        Users(full_name=full_name, username=username, mobile=mobile, email=email, password=password).save()
        return redirect('/login')


class Logout(View):
    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        return redirect('/')

    def post(self, request):
        pass


class Checkout(View):
    def get(self, request):
        if 'user' in request.session:
            id = request.GET.get('id', None)
            product = Product.objects.filter(id=id).get()
            return render(request, 'home/checkout.html', {'product': product})
        return redirect('/login')

    def post(self, request):
        pass


class Payment(View):
    def get(self, request):
        if 'user' in request.session:
            id = request.GET.get('id', None)
            product = Product.objects.filter(id=id).get()
            return render(request, 'home/payment.html', {'product': product})
        return redirect('/login')

    def post(self, request):
        pass


class Success(View):
    def get(self, request):
        if 'user' in request.session:
            id = request.GET.get('id', None)
            product = Product.objects.filter(id=id).get()
            return render(request, 'home/success.html', {'product': product})
        return redirect('/login')

    def post(self, request):
        pass