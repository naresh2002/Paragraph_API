from django.urls import path
from .views import signup, CustomTokenObtainPairView, add_paragraph

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('add_paragraph/', add_paragraph, name='add_paragraph'),
]
