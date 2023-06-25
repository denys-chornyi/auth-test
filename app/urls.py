from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from app.views import HelloView

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]