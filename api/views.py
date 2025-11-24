from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NavItemSerializer

class NavItemsAPIView(APIView):
    def get(self, request):
        nav = [
            {"name": "Home", "path": "/"},
            {"name": "About", "path": "/about"},
            {"name": "Services", "path": "/services"},
            {"name": "Contact", "path": "/contact"},
        ]

        serializer = NavItemSerializer(nav, many=True)
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .auth_serializers import RegisterSerializer


# REGISTER
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=400)


# LOGIN
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })


# GET LOGGED-IN USER
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
