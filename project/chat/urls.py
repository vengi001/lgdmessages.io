from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .steganography import messages

urlpatterns =[
    path('',views.chatPage, name="chats"),
    path('auth/login', LoginView.as_view(template_name = 'loginPage.html'), name="login-user"),
    path('auth/logout', LogoutView.as_view(), name="logout-user"),
    path('quotes/', messages.quotes, name="quotes"),
    path('sam',views.sam),
]


