from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CustomUser, Paragraph, Word
from .serializers import CustomUserSerializer, ParagraphSerializer
from django.db.models import Count
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# SIGNUP
@csrf_exempt
@swagger_auto_schema(
    method='post',
    request_body=CustomUserSerializer,
    responses={201: CustomUserSerializer, 400: 'Invalid input'}
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

# LOGIN
@csrf_exempt
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
        }
    ),
    responses={200: 'Logged in successfully', 400: 'Invalid credentials'}
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# CURRENT_USER
@swagger_auto_schema(
    method='get',
    responses={200: CustomUserSerializer}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# ADD_PARAGRAPH
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'paragraph': openapi.Schema(type=openapi.TYPE_STRING, description='Text of the paragraph')
        }
    ),
    responses={201: 'Paragraph added successfully', 400: 'Invalid input'},
    security=[{'Bearer': []}]
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
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

# SEARCH_WORD
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('word', openapi.IN_PATH, description="Word to search for", type=openapi.TYPE_STRING)
    ],
    responses={200: 'Paragraphs retrieved successfully', 404: 'No paragraphs found'},
    security=[{'Bearer': []}]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_word(request, word):
    word = word.lower()

    # Find the top 10 paragraphs sorted by the count of the word
    results = Word.objects.filter(word=word).values('paragraph_id').annotate(count=Count('word')).order_by('-count')[:10]
    
    # Extract paragraph IDs from results
    paragraph_ids = [result['paragraph_id'] for result in results]

    return Response({'paragraph_ids': paragraph_ids}, status=status.HTTP_200_OK)

# LOGOUT
@swagger_auto_schema(
    method='post',
    responses={200: 'Logged out successfully'},
    security=[{'Bearer': []}]
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
