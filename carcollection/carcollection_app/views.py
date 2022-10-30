# from carcollection.carcollection_app.models import Profile
from django.shortcuts import render
from carcollection.carcollection_app.utils import get_profile


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def create_profile(request):

    context = {

    }
    return render(request, 'profile-create.html', context)


def catalogue(request):
    pass


def create_car(request):
    pass


def details_car(request, pk):
    pass


def edit_car(request, pk):
    pass


def delete_car(request, pk):
    pass


def details_profile(request, pk):
    pass


def edit_profile(request, pk):
    pass


def delete_profile(request, pk):
    pass