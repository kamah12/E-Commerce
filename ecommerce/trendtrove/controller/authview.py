from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from trendtrove.forms import CustomUserForm

# Create your views here.

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Acount Created Successfully! Login To Continue')
            return redirect('/login')
    context = {'form':form}
    return render(request, 'trendtrove/auth/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are Already Logged In')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)  

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid Password or Username')
                return redirect('/')
        return render(request, 'trendtrove/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully')
    return redirect('/')