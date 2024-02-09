from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post
from .forms import PostForm



def home(request):
    form = PostForm()
    return render(request, 'blog/home.html', {'form': form})


def post(request):
    # posts = Post.objects.filter()
    posts=Post.objects.all().values();

    return render(request, 'blog/posts.html', {'posts': posts})
def aboutus(request):
    return render(request, 'blog/aboutus.html')


# myapp/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.filter(username=username, password=password).first()
            if user:
                return redirect('home')  # Redirect to the home page
            else:
                return render(request, 'blog/login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form, 'error_message': ''})

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             UserProfile.objects.create(username=username, password=password)
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'blog/signup.html', {'form': form})
# from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if user already exists
            if UserProfile.objects.filter(username=username).exists():
                # Handle case where user already exists
                return render(request, 'blog/signup.html', {'form': form,
                                                            'error_message': 'Username already exists. Please choose a different username.'})

            # Create new user profile
            UserProfile.objects.create(username=username, password=password)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})
