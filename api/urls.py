from django.urls import path
from .views import user_list, user_detail#, obtain_auth_token, secure_view
#from .views import user_list, user_detail, MySecuredView


#jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    
    # jwt URL patterns...
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    
    #token wise
    #path('login/', obtain_auth_token, name='obtain-token'),
    #path('secure/', secure_view, name='secure-view'),
]

