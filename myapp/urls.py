from django.urls import path
from .views import index, add_item, user_login, user_regiter, user_logout

urlpatterns =[
    path('', index, name="index"),
    path('add_item', add_item, name="add_item"),
    path('user_login', user_login, name="login"),
    path('user_register', user_regiter, name="register"),
    path('user_logout', user_logout, name="logout")
]   