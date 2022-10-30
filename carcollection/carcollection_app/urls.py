from django.urls import path, include

from carcollection.carcollection_app.views import index, catalogue, create_car, details_car, edit_car, delete_car, \
    details_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', create_car, name='create_car'),
        path('<int:pk>/', include([
            path('details/', details_car, name='details_car'),
            path('edit/', edit_car, name='edit_car'),
            path('delete/', delete_car, name='delete_car'),
        ])),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details_profile'),
        path('edit/', edit_profile, name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile'),
        path('create/', create_profile, name='create_profile'),
    ])),
)

