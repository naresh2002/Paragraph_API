from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CustomUser, Paragraph, Word
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# SIGNUP
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

# LOGIN_VIEW
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# ADD_PARAGRAPH
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_paragraph(request):
    paragraph_text = request.data.get('paragraph', '')
    user = request.user

    # Create the paragraph
    paragraph = Paragraph.objects.create(text=paragraph_text, user=user)

    # Tokenize the paragraph
    words = paragraph_text.split()
    word_counts = {}
    for word in words:
        word = word.strip('.').lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Create word entries in the database
    for word, count in word_counts.items():
        Word.objects.create(word=word, paragraph=paragraph, count=count)

    return Response({'message': 'Paragraph added successfully'}, status=status.HTTP_201_CREATED)