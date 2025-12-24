from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def api_signup(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "username and password required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "username already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response(
        {"message": "user created successfully"},
        status=status.HTTP_201_CREATED
    )


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"error": "invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key,
        "user_id": user.id,
        "username": user.username
    })


