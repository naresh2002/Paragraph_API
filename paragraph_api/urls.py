from django.urls import path
from .views import signup, CustomTokenObtainPairView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
