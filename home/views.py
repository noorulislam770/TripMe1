from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib  import messages
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    context = {
        "variable":"This is sent",
        "second_variable" : "Obviosly second variable"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        response = request.POST.get('response')
        contact = Contact(name=name,email=email,phone=phone,response=response,date=datetime.today())
        contact.save()
        messages.success(request,"Success! You will be Contacted Soon!")
    return render(request,'contact.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def Places(request):
    return render(request,'places.html')