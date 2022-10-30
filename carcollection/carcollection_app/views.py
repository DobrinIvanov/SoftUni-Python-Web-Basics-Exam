from django.shortcuts import render

# Create your views here.
# http://localhost:8000/ - index page
# http://localhost:8000/profile/create - profile create page
# http://localhost:8000/catalogue/ - catalogue page
# http://localhost:8000/car/create/ - car create page
# http://localhost:8000/car/<car-id>/details/ - car details page
# http://localhost:8000/car/<car-id>/edit/ - car edit page
# http://localhost:8000/car/<car-id>/delete/ - car delete page
# http://localhost:8000/profile/details/ - profile details page
# http://localhost:8000/profile/edit/ - profile edit page
# http://localhost:8000/profile/delete/ - profile delete page


def index(request):
    pass


def create_profile(request):
    pass


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