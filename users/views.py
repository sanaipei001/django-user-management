from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm, ProfileForm, UserUpdateForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.create(user=user)
            token = profile.generate_verification_token()
            verify_url = request.build_absolute_uri(f'/verify-email/{token}/')
            send_mail(
                'Verify Your Email',
                f'Click this link to verify your email: {verify_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            login(request, user)
            messages.success(request, 'Registration successful! Check your email to verify.')
            return redirect('verify_email', token=token)  # Pass token to URL
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def verify_email(request, token):
    profile = get_object_or_404(UserProfile, verification_token=token)
    if request.method == 'POST':
        profile.is_verified = True
        profile.verification_token = ''
        profile.save()
        messages.success(request, 'Email verified! Welcome to your dashboard.')
        return redirect('dashboard')
    return render(request, 'users/verify_email.html')

@login_required
def dashboard(request):
    if not request.user.userprofile.is_verified:
        messages.warning(request, 'Please verify your email to access the dashboard.')
        return redirect('verify_email', token=request.user.userprofile.verification_token)
    return render(request, 'users/dashboard.html')

@login_required
def profile(request):
    if not request.user.userprofile.is_verified:
        messages.warning(request, 'Please verify your email to access your profile.')
        return redirect('verify_email', token=request.user.userprofile.verification_token)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')