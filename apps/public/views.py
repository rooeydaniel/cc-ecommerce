from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(function=None, redirect_field_name=None, login_url='/login')
@require_http_methods(["GET", "POST"])
def edit_user(request):
    if request.method == "POST":
        response = {}
        response.update(csrf(request))

        id = request.POST.get('id', request.POST['id'])
        first_name = request.POST.get('first_name', request.POST['first_name'])
        last_name = request.POST.get('last_name', request.POST['last_name'])
        email = request.POST.get('email', request.POST['email'])
        username = request.POST.get('username', request.POST['username'])
        password = request.POST.get('password', request.POST['password'])
        confirm_password = request.POST.get('password2', request.POST['password2'])

        old_user = User.objects.get(pk=id)
        old_user.first_name = first_name
        old_user.last_name = last_name
        old_user.username = username
        old_user.email = email

        password_changed = False
        if password != '' and password is not None:
            if password != confirm_password:
                response['message'] = "Password and Confirm Password must match!"
                return render(request, 'edit_user.html', response)
            else:
                password_changed = True
                old_user.set_password(password)

        old_user.save()

        # If password is changed, let's log them out and force them to log in again?
        if password_changed:
            return redirect('/logout')

        request.user = User.objects.get(pk=id)
        response['message'] = "User updated successfully!"
        return render(request, 'edit_user.html', response)
    else:
        return render(request, 'edit_user.html')


@require_http_methods(["GET", "POST"])
def create_user(request):
    if request.method == "POST":
        response = {}
        response.update(csrf(request))

        first_name = request.POST.get('first_name', request.POST['first_name'])
        last_name = request.POST.get('last_name', request.POST['last_name'])
        email = request.POST.get('email', request.POST['email'])
        username = request.POST.get('username', request.POST['username'])
        password = request.POST.get('password', request.POST['password'])

        if first_name == '' or last_name == '' or email == '' or username == '' or password == '':
            response['message'] = "All form fields must contain a value."
            return render(request, 'create_user.html', response)

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['test'] = 'Registration successful!'
            return redirect('/', response)
        else:
            response['message'] = 'Login failed!'
            return render(request, 'create_user.html', response)
    else:
        user = request.user
        if user is not None and user.is_active:
            return redirect('/')
        return render(request, 'create_user.html')


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        response = {}
        response.update(csrf(request))

        username = request.POST.get('username', request.POST['username'])  # emtpy string if no username exists
        password = request.POST.get('password', request.POST['password'])  # empty string if no password exists

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['test'] = 'Testing, Testing'
            return redirect('/', response)
        else:
            response['message'] = 'Login failed!'
            return render(request, 'login.html', response)
    else:
        user = request.user
        if user is not None and user.is_active:
            return redirect('/')
        return render(request, 'login.html')


@login_required(function=None, redirect_field_name=None, login_url='/login')
@require_http_methods(["GET"])
def logout(request):
    response = {}
    auth.logout(request)

    response['message'] = 'Logout successful!'
    return render(request, 'login.html', response)


@require_http_methods(["GET"])
def home(request):
    return render(request, 'home.html')