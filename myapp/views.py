from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .models import SignUpData
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not SignUpData.objects.filter(username=username).exists():
                # Create a new SignUpData instance and save signup credentials
                signup_data = SignUpData(username=username, password=password1)
                signup_data.save()
                # Also create a new user in the Django User model
                User.objects.create_user(username=username, password=password1)
                return redirect('login')
            else:
                return render(request, 'signup.html', {'error_message': 'Username already exists'})
        else:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
@login_required
def index_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TodoItem.objects.create(title=title)
            return redirect('index')
    todo_items = TodoItem.objects.all()
    return render(request, 'index.html', {'todo_items': todo_items})


from django.shortcuts import redirect, get_object_or_404
from .models import TodoItem

@login_required
def delete_todo_view(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.delete()
    return redirect('index')

