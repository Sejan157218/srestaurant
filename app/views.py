from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from app.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from app.decoretors import unauthenticated_user

from datetime import datetime
from app.models import Addess
from app.models import Slider
from app.models import Recipes
from app.models import About
from app.models import Blog
from app.models import Blocktitle
from app.models import Client
from app.models import Contact
from app.models import Newsletter
# Create your views here.


def index(request):
    client = Client.objects.all()
    blocktitle = Blocktitle.objects.all()
    blog = Blog.objects.all().order_by("-id")
    about = About.objects.all()
    recipe = Recipes.objects.all().order_by("-id")
    data = Addess.objects.all()
    slide = Slider.objects.all().order_by("-id")
    context = {'data': data, "slide": slide,
               "recipe": recipe, 'about': about, 'blog': blog, 'blocktitle': blocktitle, 'client': client}
    if request.method == "POST":
        newsletteremail = request.POST['newsletteremail']

        newsletteremail = Newsletter(newsletteremail=newsletteremail)
        newsletteremail.save()

    return render(request, 'index.html', context)


def main(request):
    data = Addess.objects.all()
    context = {'data': data}
    return render(request, 'main.html', context)


def about(request):
    about = About.objects.all()
    data = Addess.objects.all()
    context = {'data': data, 'about': about}
    return render(request, 'about.html', context)


def blog(request):
    blog = Blog.objects.all().order_by("-id")
    blocktitle = Blocktitle.objects.all()
    data = Addess.objects.all()
    context = {'data': data, 'blocktitle': blocktitle, 'blog': blog}
    return render(request, 'blog.html', context)


def recipe(request):
    recipe = Recipes.objects.all().order_by("-id")
    data = Addess.objects.all()
    context = {'data': data, "recipe": recipe}
    return render(request, 'recipe.html', context)


def contact(request):
    data = Addess.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone,
                          message=message, date=datetime.today())
        contact.save()

    else:
        return render(request, 'contact.html', {})
    return render(request, 'contact.html', {'data': data, 'name': name})


@unauthenticated_user
def signup(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Accout was created for ' + username)
            return redirect('signin')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@unauthenticated_user
def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'accounts/signin.html')


def signout(request):
    logout(request)
    return redirect('home')
