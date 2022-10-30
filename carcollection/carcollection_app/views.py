# from carcollection.carcollection_app.models import Profile
from django.shortcuts import render, redirect

from carcollection.carcollection_app.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from carcollection.carcollection_app.models import Car, Profile
from carcollection.carcollection_app.utils import get_profile


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def catalogue(request):
    cars = Car.objects.all()
    cars_count = cars.count()
    context = {
        'cars': cars,
        'count': cars_count,
    }

    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).first()
    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    instance = Car.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = EditCarForm(instance=instance)
    else:
        form = EditCarForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    instance = Car.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = DeleteCarForm(instance=instance)
    else:
        form = DeleteCarForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'car-delete.html', context)


def details_profile(request):
    user = Profile.objects.all().first()
    price_of_all_cars = sum([car.price for car in Car.objects.all()])
    context = {
        'user': user,
        'total_car_price': price_of_all_cars,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    instance = Profile.objects.all().first()
    if request.method == 'GET':
        form = EditProfileForm(instance=instance)
    else:
        form = EditProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('details_profile')

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    instance = Profile.objects.all().first()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=instance)
    else:
        form = DeleteProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
