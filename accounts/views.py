from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm, AccountUpdateForm

# Create your views here.

def registration(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)




def logout_user(request):
    logout(request)
    return redirect('index')


def login_user(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


def update_acount(request):
    if not request.user.is_authenticated:
        return redirect("index")
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    form = AccountUpdateForm(
        initial={
            "email":request.user.email,
            "username":request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "phone_number": request.user.phone_number
        }
    )

    context['update_form'] = form
    return render(request, 'accounts/update.html', context)
