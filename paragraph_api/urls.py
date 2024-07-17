from django.urls import path
from .views import signup, CustomTokenObtainPairView, add_paragraph, search_word

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('add_paragraph/', add_paragraph, name='add_paragraph'),
    path('search_word/<str:word>/', search_word, name='search_word'),
]
