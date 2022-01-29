from .views import GetMessagesAPI, SendMessageAPI, CreateUserAPI
from django.urls import path

urlpatterns = [
    path('get-message/', GetMessagesAPI.as_view()),
    path('send-message/', SendMessageAPI.as_view()),
    path('register/', CreateUserAPI.as_view()),
]