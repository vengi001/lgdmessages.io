from django.urls import re_path , include
from .consumers import chatconsumer

websocket_urlpatterns = [
	re_path("" , chatconsumer.ChatConsumer.as_asgi()) , 
]
