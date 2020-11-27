from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from shopApp.models import Store
from datetime import datetime




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Create Order # JO3T
            if (user_form.cleaned_data['has_store']):

                Store.objects.create(name=new_user.username+'-Store')
            #Store.object.get_object_or_404()
            # Save the User object
                new_user.save()
                Profile.objects.create(
                user=new_user,
                store=Store.objects.get(name=new_user.username+'-Store'),
                address=str(user_form.cleaned_data['address']),
                country=str(user_form.cleaned_data['country']),
                city=str(user_form.cleaned_data['city']),
                street=str(user_form.cleaned_data['street']),
                zip_code=str(user_form.cleaned_data['zip_code']),
                phone=str(user_form.cleaned_data['phone']),
                date_of_birth=str(user_form.cleaned_data['date_of_birth'])
                )
            else:
                print('================================')
                print(str(user_form.cleaned_data['address']))
                new_user.save()
                Profile.objects.create(
                user=new_user,
                address=str(user_form.cleaned_data['address']),
                country=str(user_form.cleaned_data['country']),
                city=str(user_form.cleaned_data['city']),
                street=str(user_form.cleaned_data['street']),
                zip_code=str(user_form.cleaned_data['zip_code']),
                phone=str(user_form.cleaned_data['phone']),
                date_of_birth=str(user_form.cleaned_data['date_of_birth'])
                )
            # Create the user profile

            #Profile.set_store(new_user.username+'-Store')
            #Profile.save()

            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})





@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'registration/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
