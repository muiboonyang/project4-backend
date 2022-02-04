from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AccountSerializer

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken


# Putting info in payload: username, token, shows in API
# Serializer class
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['surname'] = user.surname
        token['email'] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Create new user
class CreateUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response('Error with creating user')
