from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import *
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.template import loader  
from knox.models import AuthToken
from django.shortcuts import redirect
from .serializers import UserSerializer, RegisterSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_pdf(request):
    return render(request,'login.html')
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def home(request):
    
    return render(request,'home.html')


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        context = {
            'user': user.username
        }
        return redirect(home)
        # return super(LoginAPI, self).post(request, format=None)


