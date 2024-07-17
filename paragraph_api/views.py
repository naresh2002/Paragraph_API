from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm, LoginForm
from .models import User
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = SignUpForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = LoginForm(data)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(name=name)
                if check_password(password, user.password):
                    request.session['user_name'] = user.name
                    request.session.save()
                    return JsonResponse({'message': 'Login successful'}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid name or password'}, status=400)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid name or password'}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
